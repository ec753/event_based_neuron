import numpy as np
import os

from neuron import h
from neuron.units import mV, ms
h.load_file("stdrun.hoc")
h.load_file("stdlib.hoc")
h.load_file("import3d.hoc")

import sys
sys.path.insert(1, "../../utils/")
import Stimuli, Pyr

# finds usable stimuli location initializations
# e.g. stimuli initializations that result in models with reasonable spike rates

duration = 10_000
num_cells = 10
data_dir = '../../data/morpho/segment_arrays/'

print('creating stimuli')
stim_params = Stimuli.ExperimentalStimParams()
stim_scaffold = stim_params.stim_scaffold['pyr']
segment_arrays = [np.random.randint(0, 192, len(stim_scaffold['stim_type_array'])) for _i in range(num_cells)]
stimuli_sets = [
    Stimuli.MorphoStimuli(
        f'stimset{_i}',
        stim_scaffold['stim_type_array'],
        segment_arrays[_i], stim_scaffold,
        duration
    ) for _i in range(num_cells)
]

print('initializing cells')
cells = [Pyr.Pyr(recording=False) for _i in range(num_cells)]

print('connecting stimuli')
for stimuli, cell in zip(stimuli_sets, cells):
    cell.add_stimuli(stimuli)

print('running simulation')
h.celsius = 35
h.finitialize()
h.continuerun(duration * ms)
print('simulation ended')

print('saving segment locs')
for segment_array, cell in zip(segment_arrays, cells):
    spike_rate = (len(cell.spike_times) / (duration/1000))
    if spike_rate > 0:
        # save segment_array
        unique_id = len(os.listdir())
        np.save(f'{data_dir}segment_array_{spike_rate}Hz_ID{unique_id}.npy', segment_array)