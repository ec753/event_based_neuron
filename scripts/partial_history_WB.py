import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import json
from scipy import stats
import matplotlib.lines as lines
import matplotlib as mpl

sys.path.insert(1, "../utils/")
import WB, Stimuli

from neuron import h
h.load_file("stdrun.hoc")
from neuron.units import mV, ms

########## HYPERPARAMETERS ##########
data_dir = '../data/partial_history_WB/'
num_input_patterns_per_n = 1000
num_histories = 1000
#ns = [n for n in range(3,31)]
ns = [n for n in range(42,51)]

excitatory_interval = 5
inhibitory_interval = 15

########## STIMULI ##########
print('generating stimuli')
stimuli = {}

for n in ns:
    stimuli[n] = {}
    for pattern_ind in range(num_input_patterns_per_n):
        stimuli[n][pattern_ind] = Stimuli.excitatory_and_inhibitory_n(excitatory_interval, inhibitory_interval, n)

with open(data_dir + "stimuli.json", "w") as fout:
    fout.write(json.dumps(stimuli))

########## HISTORIES ##########
print('generating histories')
histories_sim_duration = 10000
stim_params = Stimuli.ExperimentalStimParams()

df, spikes, stims = WB.run_poisson_sim(
    [stim_params.stim_scaffold['wb']['ex'], stim_params.stim_scaffold['wb']['in']], histories_sim_duration)

history_inds = np.random.randint(250, (histories_sim_duration*40)-250, num_histories)
histories_wb = np.array(
    [
        [df['v'][history_ind] for history_ind in history_inds],
        [df['m'][history_ind] for history_ind in history_inds],
        [df['h'][history_ind] for history_ind in history_inds],
    ]
)

np.save(data_dir+'histories_wb', histories_wb)
########## EXPERIMENT ##########
print('starting experiment')

# stim scaffold is used to dynamically generate stim objects for the simulation
stim_scaffold = Stimuli.ExperimentalStimParams()
stim_scaffold = stim_scaffold.stim_scaffold

# stim scaffolds
estims = stim_params.stim_scaffold['wb']['ex']
istims = stim_params.stim_scaffold['wb']['in']

for n in ns:
    for pattern_ind in range(num_input_patterns_per_n):
        print(f'n {n}/{max(ns)}, pattern {pattern_ind}/{num_input_patterns_per_n}')
        results = []
        stim_duration = max([t for stim_type, t in stimuli[n][pattern_ind]])  # total duration of the stimuli

        estims.stim_times = [stim[1] for stim in stimuli[n][pattern_ind] if stim[0] == 'e']
        istims.stim_times = [stim[1] for stim in stimuli[n][pattern_ind] if stim[0] == 'i']

        cells = {}
        fInitializeHandlers = []

        for history_ind in range(num_histories):
            history = histories_wb[:, history_ind]

            cells[history_ind] = WB.WB()
            cells[history_ind].add_custom_stimulus(estims)
            cells[history_ind].add_custom_stimulus(istims)
            cells[history_ind].sim_init(v0=history[0], m0=history[1], h0=history[2])

            fInitializeHandlers.append(h.FInitializeHandler(cells[history_ind].do_sim_init))

        h.finitialize()
        h.continuerun(stim_duration + 20)

        for history_ind in range(num_histories):
            nsts = [spike - stim_duration for spike in list(cells[history_ind].spike_times)]
            nsts = [nst for nst in nsts if nst > 0]
            if len(nsts) < 1:
                results.append(np.nan)
            else:
                results.append(min(nsts))

        np.save(f'{data_dir}results/wb_{n}_{pattern_ind}', np.array(results))

    print()
