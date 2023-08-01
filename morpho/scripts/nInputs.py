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


segment_arrayID = 'ID96'
n = 5
data_dir = '../../data/morpho/'
duration = 100
extra_duration = 20


def run_event_sim(stimuli, last_stimulus, extra_duration):
    print(f'pooled event_sim: {last_stimulus + extra_duration}')
    print(f'initializing cell')
    pyr = Pyr.Pyr()
    #pyr.initialize_state_vars(history) #TODO
    print(f'adding stimuli')
    pyr.add_stimuli(stimuli)
    
    #h.CVode().active(True)
    h.celsius = 35
    print(f'celcius set')
    time.sleep(2)
    h.finitialize()
    print(f'finitialized')
    time.sleep(2)
    h.continuerun(last_stimulus + extra_duration)
    print(f'spikes: {list(pyr.spike_times)}')
    nsts = [nst for nst in list(pyr.spike_times) if nst > last_stimulus]

    print()

    os.wait()
    if len(nsts) == 0:
        return np.inf
    else:
        return nsts[0]

def pyonevent(stim_times):
    start_time = time.time()
    stim_times = neuron.numpy_from_pointer(stim_times, 50*30)
    stim_times = stim_times.reshape([30,50])[:,:n]
    #stim_times = stim_times - np.min(stim_times[stim_times > 0])
    print(f'stim_times: {stim_times.shape}')
    #print(f'{np.min(stim_times[stim_times > 0])}')
    # change the stimuli
    for i in range(30):
        stimuli.stimuli[i].event_times = list(stim_times[i, :])
    
    # pool is used to parallelize
    nst = pool.starmap(
        run_event_sim,
        [
            [
                stimuli, duration, extra_duration #stimuli, (np.nanmax(stim_times)+50), extra_duration
            ]
        ]
    )[0]
    
    print(nst)
    print(f'simulation time: {np.nanmax(stim_times) + extra_duration}')
    print(f'real time: {time.time() - start_time}')
    print()
    return nst


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
    print('generating stimuli')
    stim_locs_file = [file for file in os.listdir(f'{data_dir}segment_arrays/') if segment_arrayID+'.npy' in file][0]
    print(stim_locs_file)

    stim_params = Stimuli.ExperimentalStimParams()
    stim_scaffold = stim_params.stim_scaffold['pyr']
    stim_locs = np.load(f'{data_dir}segment_arrays/{stim_locs_file}')

    stimuli = Stimuli.MorphoStimuli('stimuli',stim_scaffold['stim_type_array'],stim_locs, stim_scaffold, duration)

    num_events = sum([len(stimulus.event_times) for stimulus in stimuli.stimuli])
    print(f'total number of events: {num_events}')

    try: os.mkdir(f'{data_dir}nInputs_stimuli') 
    except: pass
    with open(f'{data_dir}nInputs_stimuli/morpho_stimuli_{segment_arrayID}_{n}.pkl', 'wb') as handle:
        pkl.dump(stimuli, handle, protocol=pkl.HIGHEST_PROTOCOL)


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

    pool.close()



