import sys
import json
import numpy as np
sys.path.insert(1, "../utils/")
import HH, Stimuli
from neuron import h
h.load_file("stdrun.hoc")
from neuron.units import mV, ms
import time

'''
The partial histories scripts first generate stimuli patterns, then random cell histories (state variable frames) and 
then run experiments simulating the combination of each of the stimuli patterns with each of the histories with each 
value of n for n inputs. The results allow for the statistical analysis of response distributions given ambiguity in 
initial conditions and differing quanta of input stimuli. 
'''

########## HYPERPARAMETERS ##########
data_dir = '../data/partial_history/'
num_input_patterns_per_n = 1000
num_histories = 1000

excitatory_interval = 5
inhibitory_interval = 15

ns = [n for n in range(3,51)]
stim_types = ['base','lw','lt','lwlt','burst']
########## STIMULI ##########
print('generating stimuli')
stimuli = {}

for n in ns:
    stimuli[n] = {}
    for pattern_ind in range(num_input_patterns_per_n):
        stimuli[n][pattern_ind] = Stimuli.excitatory_and_inhibitory_n(excitatory_interval, inhibitory_interval, n)

with open(data_dir + "stimuli_31_51.json", "w") as fout:
    fout.write(json.dumps(stimuli))

########## HISTORIES ##########
print('generating histories')
histories_sim_duration = 10000
stim_params = Stimuli.ExperimentalStimParams()
stim_scaffold = stim_params.stim_scaffold

histories = {}
history_inds = np.random.randint(250, (histories_sim_duration*40)-250, num_histories)
for stim_type in stim_types:
    df, spikes, stims = HH.run_poisson_sim(
        [stim_params.stim_scaffold[stim_type]['ex'], stim_params.stim_scaffold[stim_type]['in']],
        None, histories_sim_duration)

    histories[stim_type] =  np.array(
        [
            [df['v'][history_ind] for history_ind in history_inds],
            [df['m'][history_ind] for history_ind in history_inds],
            [df['h'][history_ind] for history_ind in history_inds],
            [df['n'][history_ind] for history_ind in history_inds],
        ]
    )
    np.save(f'{data_dir}histories_{stim_type}', histories[stim_type])

########## EXPERIMENT ##########
print('starting experiment')

for n in ns:
    for pattern_ind in range(num_input_patterns_per_n):
        print(f'n {n}/{max(ns)}, pattern {pattern_ind}/{num_input_patterns_per_n}')
        results = {stim_type:[] for stim_type in stim_types}

        etimes = [stim[1] for stim in stimuli[n][pattern_ind] if stim[0] == 'e']
        itimes = [stim[1] for stim in stimuli[n][pattern_ind] if stim[0] == 'i']

        stim_duration = max([t for stim_type, t in stimuli[n][pattern_ind]])  # total duration of the stimuli

        cells = {}
        fInitializeHandlers = []

        for stim_type in stim_types:
            stim_scaffold[stim_type]['ex'].stim_times = etimes
            stim_scaffold[stim_type]['in'].stim_times = itimes

            cells[stim_type] = {}
            for history_ind in range(num_histories):
                history = histories[stim_type][:, history_ind]

                cells[stim_type][history_ind] = HH.HH()
                cells[stim_type][history_ind].add_custom_stimulus(stim_scaffold[stim_type]['ex'])
                cells[stim_type][history_ind].add_custom_stimulus(stim_scaffold[stim_type]['in'])
                cells[stim_type][history_ind].sim_init(
                    v0=history[0],
                    m0=history[1],
                    h0=history[2],
                    n0=history[3]
                )
                fInitializeHandlers.append(h.FInitializeHandler(cells[stim_type][history_ind].do_sim_init))

        h.finitialize(-65)
        h.continuerun(stim_duration + 20 * ms)

        for stim_type in stim_types:
            for history_ind in range(num_histories):
                nsts = [spike - stim_duration for spike in list(cells[stim_type][history_ind].spike_times)]
                nsts = [nst for nst in nsts if nst > 0]
                if len(nsts) < 1:
                    results[stim_type].append(np.nan)
                else:
                    results[stim_type].append(min(nsts))
            np.save(f'{data_dir}results/{stim_type}_{n}_{pattern_ind}', np.array(results[stim_type]))
