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
ns = [n for n in range(3, 21)]
num_histories = 1000
excitatory_interval = 5
inhibitory_interval = 15
num_input_patterns = 100

experiment_id = np.random.randint(1000000000) # used to give every experiment a unique id as to not write over data

out_dir = './data/nst_distribution_evolution/'

########## LOAD HISTORIES ##########
histories_data_dir = './data/nst_distribution_evolution/'
histories_sets = {
    'base': np.load(f'{histories_data_dir}histories_base.npy'),
    'lw': np.load(f'{histories_data_dir}histories_lw.npy'),
    'lt': np.load(f'{histories_data_dir}histories_lt.npy'),
    'lwlt': np.load(f'{histories_data_dir}histories_lwlt.npy'),
    'burst': np.load(f'{histories_data_dir}histories_burst.npy')
}

########## GENERATE STIMULI ##########
stimuli = {}

for i in range(num_input_patterns):
    stimuli[i] = Stimuli.excitatory_and_inhibitory_n(excitatory_interval, inhibitory_interval, max(ns))

with open(f'{out_dir}/stimuli_{experiment_id}.json', "w") as fout:
    json.dump(stimuli, fout)

########## RUN EXPERIMENT ##########
stim_params = Stimuli.ExperimentalStimParams()
stim_scaffold = stim_params.stim_scaffold

for stim_type in stim_scaffold:
    for stim_pattern_ind in range(num_input_patterns):
        print(" "*(len(stim_type) + len(str(stim_pattern_ind)) + 2) + '_' * len(ns))
        print(f'{stim_type} {stim_pattern_ind}:', end='')
        stim_pattern = stimuli[stim_pattern_ind]
        results = {n:[] for n in ns}
        for n in ns:
            _stims = stim_pattern[-n:]

            # run a bunch of cells in parallel
            stim_min = min([t for stim_type, t in _stims])


            _e_times = [t - stim_min for stim_type, t in _stims if stim_type == 'e']
            _i_times = [t - stim_min for stim_type, t in _stims if stim_type == 'i']

            stim_duration = max(_e_times + _i_times) # total duration of the stimuli

            cells = {}
            fInitializeHandlers = []

            for history_ind in range(num_histories):
                history = histories_sets[stim_type][:, history_ind]
                cells[history_ind] = HH.HH()
                stim_scaffold[stim_type]['ex'].stim_times = _e_times
                stim_scaffold[stim_type]['in'].stim_times = _i_times
                cells[history_ind].add_custom_stimulus(stim_scaffold[stim_type]['ex'])
                cells[history_ind].add_custom_stimulus(stim_scaffold[stim_type]['in'])
                cells[history_ind].sim_init(
                    v0 = history[0],
                    m0 = history[1],
                    h0 = history[2],
                    n0 = history[3]
                )
                fInitializeHandlers.append(h.FInitializeHandler(cells[history_ind].do_sim_init))

            h.finitialize(-65)
            h.continuerun(stim_duration + 20 * ms)

            for history_ind in range(num_histories):
                nsts = [spike - stim_duration for spike in list(cells[history_ind].spike_times)]
                nsts = [nst for nst in nsts if nst > 0]
                if len(nsts) < 1:
                    results[n].append(np.nan)
                else:
                    results[n].append(min(nsts))
            print(']',end='')
        with open(f'{out_dir}results/{stim_type}_{experiment_id}_{stim_pattern_ind}.json', "w") as fout:
            json.dump(results, fout)
        print()