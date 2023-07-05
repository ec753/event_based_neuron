from neuron import h
from neuron.units import mV, ms
import numpy as np
import queue
import json
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

# creates stimuli sets that result in spiking models
duration = 5000  # any longer than 10000 is a bit fraught, there are lots of state variables to keep track of
data_dir = '../data/state_reconstruct_morpho/'
num_cells = 5

print('generating cells')
cells = [Morpho.Pyramidal("../morphology/c91662.CNG.swc", record_spiking_histories=True) for i in range(num_cells)]
stim_params = [Stimuli.MorphoStimParams(cell) for cell in cells]
stimuli = [Stimuli.place_stims_along_morphology(stim_param.stim_scaffold, duration=duration) for stim_param in stim_params]

print('connecting stimuli')
for _cell, _stimuli in zip(cells,stimuli):
    for seg in _stimuli:
        _cell.connect_input(_stimuli[seg], _cell.all_input_segments[seg])

print('running simulation')
h.finitialize(-65)
h.continuerun(duration)

print('saving results')
for i, cell in enumerate(cells):
    if len(cell.spike_times) > 20:
        num_stim_sets = len(os.listdir(f'{data_dir}stimuli_sets/'))

        # write stimuli to file
        with open(f'{data_dir}stimuli_sets/stimuli_set_{num_stim_sets}.pkl', 'wb') as handle:
            pkl.dump(stimuli[i], handle, protocol=pkl.HIGHEST_PROTOCOL)

        # save spike histories
        with open(f'{data_dir}spiking_histories/spiking_histories_{num_stim_sets}.pkl', 'wb') as handle:
            pkl.dump(cell.spiking_histories, handle, protocol=pkl.HIGHEST_PROTOCOL)





