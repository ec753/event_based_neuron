import sys
import json
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(1, "./utils/")
import HH, Stimuli
from neuron import h
h.load_file("stdrun.hoc")
from neuron.units import mV, ms

import time

########## HYPERPARAMETERS ##########
data_dir = './data/partial_history/'
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

df_base, spikes, stims = HH.run_poisson_sim([stim_params.ex_base, stim_params.in_base])
df_lw, spikes, stims = HH.run_poisson_sim([stim_params.ex_lw, stim_params.in_lw])
df_lt, spikes, stims = HH.run_poisson_sim([stim_params.ex_lt, stim_params.in_lt])
df_lwlt, spikes, stims = HH.run_poisson_sim([stim_params.ex_lwlt, stim_params.in_lwlt])
df_burst, spikes, stims = HH.run_poisson_sim([stim_params.ex_burst, stim_params.in_burst])

history_inds = np.random.randint(250, 400000-250, num_histories)
histories_base = np.array(
    [
        [df_base['v'][history_ind] for history_ind in history_inds],
        [df_base['m'][history_ind] for history_ind in history_inds],
        [df_base['h'][history_ind] for history_ind in history_inds],
        [df_base['n'][history_ind] for history_ind in history_inds],
    ]
)
histories_lw = np.array(
    [
        [df_lw['v'][history_ind] for history_ind in history_inds],
        [df_lw['m'][history_ind] for history_ind in history_inds],
        [df_lw['h'][history_ind] for history_ind in history_inds],
        [df_lw['n'][history_ind] for history_ind in history_inds],
    ]
)
histories_lt = np.array(
    [
        [df_lt['v'][history_ind] for history_ind in history_inds],
        [df_lt['m'][history_ind] for history_ind in history_inds],
        [df_lt['h'][history_ind] for history_ind in history_inds],
        [df_lt['n'][history_ind] for history_ind in history_inds],
    ]
)
histories_lwlt = np.array(
    [
        [df_lwlt['v'][history_ind] for history_ind in history_inds],
        [df_lwlt['m'][history_ind] for history_ind in history_inds],
        [df_lwlt['h'][history_ind] for history_ind in history_inds],
        [df_lwlt['n'][history_ind] for history_ind in history_inds],
    ]
)
histories_burst = np.array(
    [
        [df_burst['v'][history_ind] for history_ind in history_inds],
        [df_burst['m'][history_ind] for history_ind in history_inds],
        [df_burst['h'][history_ind] for history_ind in history_inds],
        [df_burst['n'][history_ind] for history_ind in history_inds],
    ]
)

histories_sets = {
    'base': histories_base,
    'lw': histories_lw,
    'lt': histories_lt,
    'lwlt': histories_lwlt,
    'burst': histories_burst
}

print('writing histories to file')
np.save(data_dir+'histories_base', histories_base)
np.save(data_dir+'histories_lw', histories_lw)
np.save(data_dir+'histories_lt', histories_lt)
np.save(data_dir+'histories_lwlt', histories_lwlt)
np.save(data_dir+'histories_burst', histories_burst)
