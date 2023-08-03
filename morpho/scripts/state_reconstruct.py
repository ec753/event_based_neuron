import numpy as np
import json
import ctypes
import os

from neuron import h
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
parser.add_argument('data_dir', type=str, help='directory to dump results to')
parser.add_argument('duration', type=float, help='duration of the simulation')
parser.add_argument('n', type=int, help='number of reconstructions to do')
args = parser.parse_args()

uniqueID = args.uniqueID #'0' 
segment_arrayID = args.segment_arrayID #'ID96'
data_dir = args.data_dir #'../../data/morpho/'
duration = args.duration #200
n = args.n #1


histories_files = [file for file in os.listdir(f'{data_dir}random_histories/') if segment_arrayID+'.json' in file]
#=print(f'histories: {len(histories_files)}')

origin_simulations = [Pyr.Pyr(vm_recording=True) for i in range(n)]
reconstruct_simulations = [Pyr.Pyr(vm_recording=True) for i in range(n)]

stim_locs_file = [file for file in os.listdir(f'{data_dir}segment_arrays/') if segment_arrayID+'.npy' in file][0]
print(stim_locs_file)

stim_params = Stimuli.ExperimentalStimParams()
stim_scaffold = stim_params.stim_scaffold['pyr']
stim_locs = np.load(f'{data_dir}segment_arrays/{stim_locs_file}')

stimuli_sets = [
    Stimuli.MorphoStimuli(
        f'stimset',
        stim_scaffold['stim_type_array'],
        stim_locs, stim_scaffold,
        duration
    ) for i in range(n)]

def _initer(simdata, history):
    simdata.initialize_state_vars(history)

fihs = [] # holds finitializehandlers
for i in range(n):
    origin_simulations[i].add_stimuli(stimuli_sets[i])
    reconstruct_simulations[i].add_stimuli(stimuli_sets[i])
    history_inds = np.random.choice(len(histories_files), 2)
     
    with open(f'{data_dir}random_histories/{histories_files[history_inds[0]]}') as fin:
        history_origin = json.load(fin)
    
    with open(f'{data_dir}random_histories/{histories_files[history_inds[1]]}') as fin:
        history_reconstruct = json.load(fin)
    '''
    for seg in history_origin:
        print(history_origin[seg]['v'])
        print(history_reconstruct[seg]['v'])
    '''
    origin_simulations[i].initialize_state_vars(history_origin)
    reconstruct_simulations[i].initialize_state_vars(history_reconstruct)
    fihs.append(h.FInitializeHandler(lambda: (lambda i:_initer(origin_simulations[i], history_origin))(i))) # .initialize_state_vars(history_origin)))
    fihs.append(h.FInitializeHandler(lambda: (lambda i: _initer(reconstruct_simulations[i], history_reconstruct))(i)))

print('running simulations')
h.celsius = 35

h.finitialize()
h.continuerun(duration)

print('writing results to file')
try: os.mkdir(f'{data_dir}reconstruct')
except: pass

origin_vs = np.array([cell._vs for cell in origin_simulations])
reconstruct_vs = np.array([cell._vs for cell in reconstruct_simulations])

np.save(f'{data_dir}reconstruct/origin_v_{segment_arrayID}_{uniqueID}.npy', origin_vs)
np.save(f'{data_dir}reconstruct/reconstruct_v_{segment_arrayID}_{uniqueID}.npy', reconstruct_vs)