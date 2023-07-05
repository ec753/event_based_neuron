from neuron import h
from neuron.units import mV, ms
import numpy as np
import queue
import json
import gc
import os
import time
import pickle as pkl

import sys
sys.path.insert(1, "../utils/")
import Morpho, Stimuli

h.load_file("stdrun.hoc")
h.load_file("stdlib.hoc")
h.load_file("import3d.hoc")
h.load_file("stdrun.hoc")

reconstruct_duration = 250
data_dir = '../data/state_reconstruct_morpho/'
num_cell_pairs = 5 # we will be simulating num_cell_pairs * 2 cells

# load a matching stimuli_set and spiking_histories
ind = 0

with open(f'{data_dir}stimuli_sets/stimuli_set_{ind}.pkl', 'rb') as handle:
    stimuli = pkl.load(handle)

with open(f'{data_dir}spiking_histories/spiking_histories_{ind}.pkl', 'rb') as handle:
    spiking_histories = pkl.load(handle)

print('generating cells')
# create origin and reconstruct cells, each initiated with different spiking histories
cells_0 = [Morpho.Pyramidal("../morphology/c91662.CNG.swc") for i in range(num_cell_pairs)]
stim_params_0 = [Stimuli.MorphoStimParams(cell) for cell in cells_0]

cells_1 = [Morpho.Pyramidal("../morphology/c91662.CNG.swc") for i in range(num_cell_pairs)]
stim_params_1 = [Stimuli.MorphoStimParams(cell) for cell in cells_1]

print('connecting and initializing cells')

for cell0, cell1 in zip(cells_0, cells_1):
    # connect stimuli in same patterns
    for seg in stimuli:
        cell0.connect_input(stimuli[seg], cell0.all_input_segments[seg])
        cell1.connect_input(stimuli[seg], cell1.all_input_segments[seg])

    # initialize with different spiking histories
    history_inds = np.random.randint(0, len(spiking_histories), 2)
    cell0.set_initialize_state(spiking_histories[history_inds[0]])
    cell1.set_initialize_state(spiking_histories[history_inds[1]])

print('starting simulation')
h.finitialize(-65)
h.continuerun(reconstruct_duration)

print('writing results')
cell_count = 0
for cell0, cell1 in zip(cells_0, cells_1):
    v0 = np.array([list(vec) for vec in cell0.v])
    v1 = np.array([list(vec) for vec in cell1.v])

    np.save(f'{data_dir}results/cellv_{ind}_{cell_count}_0.npy', v0)
    np.save(f'{data_dir}results/cellv_{ind}_{cell_count}_1.npy', v1)
    cell_count += 1


