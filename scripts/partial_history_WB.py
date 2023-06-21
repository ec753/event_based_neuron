import sys
import json
import time
import argparse
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(1, "../utils/")
import WB, Stimuli
from neuron import h
h.load_file("stdrun.hoc")
from neuron.units import mV, ms

########## HYPERPARAMETERS ##########
'''
parser = argparse.ArgumentParser(description='Args')
parser.add_argument('n', type=int, help='n')
args = parser.parse_args()
n = args.n
'''

data_dir = '../data/partial_history_WB/'
num_input_patterns_per_n = 1000
num_histories = 1000
ns = [n for n in range(3,31)]

excitatory_interval = 5
inhibitory_interval = 15

########## STIMULI ##########
print('loading stimuli')

with open(f'{data_dir}stimuli.json') as f:
    stimuli = json.load(f)
########## HISTORIES ##########
print('loading histories')

histories_wb = np.load(f'{data_dir}histories_wb.npy')

histories_sets = {
    'wb': histories_wb
}

########## EXPERIMENT ##########
print('starting experiment')

# stim scaffold is used to dynamically generate stim objects for the simulation
stim_scaffold = Stimuli.ExperimentalStimParams()
stim_scaffold = stim_scaffold.stim_scaffold

for n in ns:
    print(f'running experiments with {n} inputs')
    for pattern_ind in range(num_input_patterns_per_n):
    #for pattern_ind in [50]:
        print(f'progress for this n = {n}: {pattern_ind}/{num_input_patterns_per_n}')

        start_time = time.time()

        _stims = stimuli[str(n)][str(pattern_ind)]
        _stims = [(stim_type, float(t)) for stim_type, t in _stims]
        # run a bunch of cells in parallel
        stim_duration = max([t for stim_type, t in _stims])  # total duration of the stimuli

        _e_times = [t for stim_type, t in _stims if stim_type == 'e']
        _i_times = [t for stim_type, t in _stims if stim_type == 'i']

        cells = {}
        fInitializeHandlers = []

        print(f'setting up {len(histories_sets) * num_input_patterns_per_n * num_histories} cells')
        for stim_type in histories_sets:
            cells[stim_type] = {}
            for history_ind in range(num_histories):
                history = histories_sets[stim_type][:, history_ind]

                cells[stim_type][history_ind] = WB.WB()
                stim_scaffold[stim_type]['ex'].stim_times = _e_times
                stim_scaffold[stim_type]['in'].stim_times = _i_times
                cells[stim_type][history_ind].add_custom_stimulus(stim_scaffold[stim_type]['ex'])
                cells[stim_type][history_ind].add_custom_stimulus(stim_scaffold[stim_type]['in'])
                cells[stim_type][history_ind].sim_init(
                    v0=history[0],
                    m0=history[1],
                    h0=history[2],
                )
                fInitializeHandlers.append(h.FInitializeHandler(cells[stim_type][history_ind].do_sim_init))

        print(f'running simulation')
        h.finitialize(-65)
        h.continuerun(stim_duration + 20 * ms)
        print(f'simulation ended')
        print(f'recording results')
        for stim_type in histories_sets:
            results = []
            for history_ind in range(num_histories):
                nsts = [spike - stim_duration for spike in list(cells[stim_type][history_ind].spike_times)]
                nsts = [nst for nst in nsts if nst > 0]
                if len(nsts) < 1:
                    results.append(np.nan)
                else:
                    results.append(min(nsts))
            np.save(f'{data_dir}results/{stim_type}_{n}_{pattern_ind}', np.array(results))

        print(f'batch took {round(time.time() - start_time, 1)} sec')
        print()
print()
