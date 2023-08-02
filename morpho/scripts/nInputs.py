import numpy as np
import queue
import json
import ctypes
import os
import time
import pickle as pkl
import multiprocessing

import neuron
from neuron import nrn_dll_sym, h
from neuron.units import ms, mV
h.load_file("stdrun.hoc")
h.load_file("stdlib.hoc")
h.load_file("import3d.hoc")

import sys
sys.path.insert(1, "../../utils/")
import Stimuli, Pyr

import argparse
parser = argparse.ArgumentParser(description='Args')
parser.add_argument('uniqueID', type=str, help='unique id added to file to avoid collisions while parallelizing')
parser.add_argument('segment_arrayID', type=str, help='ID of the stim_locs_file made from initialize_stimuli_locs.py')
parser.add_argument('stim_times_file', type=str, help='file to times of the stimuli, writes one if it DNE')
parser.add_argument('n', type=int, help='number of inputs')
parser.add_argument('data_dir', type=str, help='directory to dump results to')
parser.add_argument('duration', type=float, help='duration of the simulation')
parser.add_argument('extra_duration', type=float, help='duration added to each onevent simulation')
args = parser.parse_args()

uniqueID = args.uniqueID #'0' 
segment_arrayID = args.segment_arrayID #'ID96'
stim_times_file = args.stim_times_file #'../../data/morpho/nInputs_stimuli/stim_times_0.json'
n = args.n #5
data_dir = args.data_dir #'../../data/morpho/'
duration = args.duration #100
extra_duration = args.extra_duration #20


def run_event_sim(stimuli, last_stimulus, extra_duration):
    pyr = Pyr.Pyr()
    # initialize with random history
    #history_ind = np.random.randint(len(histories))
    #pyr.initialize_state_vars(histories[history_ind]) 
    '''
    for stimulus in stimuli.stimuli:
        print(stimulus.event_times)
    '''
    pyr.add_stimuli(stimuli)
    
    h.CVode().active(True)
    h.celsius = 35
    h.finitialize()
    h.continuerun(last_stimulus + extra_duration)
    #print(f'spikes: {list(pyr.spike_times)}')
    nsts = [nst for nst in list(pyr.spike_times) if nst > last_stimulus]

    if len(nsts) == 0:
        return np.inf
    else:
        return nsts[0]

def pyonevent(stim_times):
    start_time = time.time()
    stim_times = neuron.numpy_from_pointer(stim_times, 50*30)
    stim_times = stim_times.reshape([30,50])[:,:n]
    # recenter to avoid extra simulation time
    first_stim = np.min(stim_times[stim_times >= 0])
    last_stim = np.max(stim_times)
    stim_times = stim_times - first_stim
    # change the stimuli
    for i in range(30):
        stimuli.stimuli[i].event_times = sorted([stim for stim in list(stim_times[i, :]) if stim >= 0])
    
    # pool is used to parallelize
    nst = pool.starmap(
        run_event_sim,
        [
            [
                stimuli, np.max(stim_times), extra_duration
            ]
        ]
    )[0]

    nst = nst + first_stim
    time2spike = nst - last_stim
    
    print(f'nst: {nst}')
    #print(f'simulation time: {np.nanmax(stim_times) + extra_duration}')
    #print(f'real time: {time.time() - start_time}')
    print()
    return time2spike


# Set up communications between NEURON and python
double_ptr = ctypes.POINTER(ctypes.c_double)
on_event_proto = ctypes.CFUNCTYPE(ctypes.c_double, double_ptr)
# CFUNCTYPE parameters are as follows: (the return type, the input types which are 1) estims, 2) istims, 3) spikes

on_event_c = on_event_proto(pyonevent)
on_event_c_ptr = ctypes.cast(on_event_c, double_ptr)

nrn_hocobj_ptr = nrn_dll_sym("nrn_hocobj_ptr")
nrn_hocobj_ptr.restype = ctypes.py_object
event_callback_ptr = nrn_hocobj_ptr(ctypes.cast(on_event_c_ptr, double_ptr))


if __name__ == '__main__':
    print('loading stimuli')
    stim_locs_file = [file for file in os.listdir(f'{data_dir}segment_arrays/') if segment_arrayID+'.npy' in file][0]
    print(stim_locs_file)

    stim_params = Stimuli.ExperimentalStimParams()
    stim_scaffold = stim_params.stim_scaffold['pyr']
    stim_locs = np.load(f'{data_dir}segment_arrays/{stim_locs_file}')

    stimuli = Stimuli.MorphoStimuli('stimuli',stim_scaffold['stim_type_array'],stim_locs, stim_scaffold, duration)

    try: 
        # open the file
        with open(stim_times_file, 'r') as fin:
            stim_times = json.load(fin)
        # set the stim times
        for i, stimulus in enumerate(stimuli.stimuli):
            stimulus.event_times = stim_times[str(i)]
    except:
        # write the file
        print('no stim_times file found, writing file instead')
        try: os.mkdir(f'{data_dir}nInputs_stimuli') 
        except: pass
        stim_times = {i: stimulus.event_times for i, stimulus in enumerate(stimuli.stimuli)}
        with open(stim_times_file, "w") as fout:
            fout.write(json.dumps(stim_times))
    
    '''
    try: os.mkdir(f'{data_dir}nInputs_stimuli') 
    except: pass
    # save stim_times class obj
    with open(f'{data_dir}nInputs_stimuli/morpho_stimuli_{segment_arrayID}_{n}.pkl', 'wb') as handle:
        pkl.dump(stimuli, handle, protocol=pkl.HIGHEST_PROTOCOL)
    '''

    num_events = sum([len(stimulus.event_times) for stimulus in stimuli.stimuli])
    print(f'total number of events: {num_events}')

    print('loading histories')
    histories_files = [file for file in os.listdir(f'{data_dir}random_histories/') if segment_arrayID+'.json' in file]
    histories = []
    for history_file in histories_files:
        with open(f'{data_dir}random_histories/{history_file}') as fin:
            histories.append(json.load(fin))
    print(f'histories: {len(histories)}')
    print()

    pool = multiprocessing.Pool(1)

    ebneuron = h.ebneuron()
    ebneuron._ref_on_event = event_callback_ptr
    ebneuron_spikes = h.Vector()
    ebneuron_nc = h.NetCon(ebneuron, None)
    ebneuron_nc.record(ebneuron_spikes)

    netstims = []
    netcons = []

    for w, stimulus in enumerate(stimuli.stimuli):
        for stim_time in stimulus.event_times:
            netstims.append(h.NetStim())
            netstims[-1].start = stim_time * ms
            netstims[-1].number = 1
            netcons.append(h.NetCon(netstims[-1], ebneuron))
            netcons[-1].weight[0] = w +1 # weight (w) is used to indicate the unique location of the stimulus
            netcons[-1].delay = 0

    h.finitialize()
    h.continuerun(duration)

    #ebneuron.print()

    # write spikes to file
    print('writing results to file')
    try: os.mkdir(f'{data_dir}nInputs_spikes')
    except: pass

    np.save(f'{data_dir}nInputs_spikes/spikes_{uniqueID}_{segment_arrayID}_{n}.npy', list(ebneuron_spikes))

    pool.close()