import sys
import json
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(1, "../utils/")
import WB, Stimuli
from neuron import h
h.load_file("stdrun.hoc")
from neuron.units import mV, ms

import time

########## HYPERPARAMETERS ##########
data_dir = '../data/partial_history_WB/'
num_input_patterns_per_n = 1000
num_histories = 1000
ns = [n for n in range(3,31)]

excitatory_interval = 5
inhibitory_interval = 15

########## STIMULI ##########
print('generating stimuli')
stimuli = {}
for n in ns:
    stimuli[n] = {}
    for pattern_ind in range(num_input_patterns_per_n):
        stimuli[n][pattern_ind] = Stimuli.excitatory_and_inhibitory_n(excitatory_interval, inhibitory_interval, n)

# write to file
print('writing stimuli to file')
with open(data_dir + "stimuli.json", "w") as fout:
    fout.write(json.dumps(stimuli))\

########## HISTORIES ##########
print('generating histories')

stim_params = Stimuli.ExperimentalStimParams()

df, spikes, stims = WB.run_poisson_sim([stim_params.stim_scaffold['wb']['ex'], stim_params.stim_scaffold['wb']['ex']])

history_inds = np.random.randint(250, 400000-250, num_histories)
histories_wb = np.array(
    [
        [df['v'][history_ind] for history_ind in history_inds],
        [df['m'][history_ind] for history_ind in history_inds],
        [df['h'][history_ind] for history_ind in history_inds],
    ]
)

print('writing histories to file')
np.save(data_dir+'histories_wb', histories_wb)
