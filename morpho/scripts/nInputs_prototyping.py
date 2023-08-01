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
    h.finitialize()
    print(f'running simulation')
    h.continuerun(last_stimulus + extra_duration)
    print(f'spikes: {list(pyr.spike_times)}')
    nsts = [nst for nst in list(pyr.spike_times) if nst > last_stimulus]
    if len(nsts) == 0:
        return np.inf
    else:
        return nsts[0]

def pyonevent(stimuli):
    # used for troubleshooting
    start_time = time.time()
    # pool is used to parallelize
    nst = pool.starmap(
        run_event_sim,
        [
            [
                stimuli, duration, extra_duration
            ]
        ]
    )[0]
    
    print(nst)
    print(f'simulation time: {duration + extra_duration}')
    print(f'real time: {time.time() - start_time}')
    print()
    return nst

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

pyonevent(stimuli)

pool.close()