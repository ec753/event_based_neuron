import sys
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
sys.path.insert(1, "../utils/")
import HH, WB, Stimuli
from neuron import h
h.load_file("stdrun.hoc")
from neuron.units import mV, ms

# part 1 of the state reconstruction experiment,
# generates the origin simulation data for which to reconstruct

data_dir = '../data/state_reconstruct/original_simulation_data/'
sim_length = 1_000_000

# generate stimuli
print('generating stimuli times')
e_times = Stimuli.poisson_process_duration(5, sim_length)
i_times = Stimuli.poisson_process_duration(15, sim_length)

with open(f'{data_dir}e_times.txt', 'w') as fout:
    for t in e_times:
        fout.write(f'{t}\n')
with open(f'{data_dir}i_times.txt', 'w') as fout:
    for t in i_times:
        fout.write(f'{t}\n')

stim_params = Stimuli.ExperimentalStimParams()
stim_scaffold = stim_params.stim_scaffold

for stim_type in stim_scaffold:
    stim_scaffold[stim_type]['ex'].stim_times = e_times
    stim_scaffold[stim_type]['in'].stim_times = i_times

print('setting up HH simulations')
# the HH and WB simulations must be done separately because they run a different temperatures
simulations = {
    'base':HH.HH(),
    'lw':HH.HH(),
    'lt':HH.HH(),
    'lwlt':HH.HH(),
    'burst':HH.HH(),
}

for stim_type in simulations:
    simulations[stim_type].add_custom_stimulus(stim_scaffold[stim_type]['ex'])
    simulations[stim_type].add_custom_stimulus(stim_scaffold[stim_type]['in'])

print('running simulations')
h.finitialize(-65)
h.continuerun(sim_length * ms)

print('extracting histories')
def standarize_column(column):
    # set column to fit in (0,1)
    column = column - np.min(column)
    column = column / np.max(column)
    return column

def dist(p1, p2):
    # get distance between 2 standardized histories
    return np.sqrt(
        pow(p1['v'] - p2['v'], 2) + pow(p1['m'] - p2['m'], 2) + pow(p1['n'] - p2['n'], 2) + pow(p1['h'] - p2['h'], 2))

def isolate_spiking_histories(sim):
    spiking_histories = []
    for spike in sim.spike_times:
        row = round(40 * spike)
        spiking_histories.append(
            pd.DataFrame(
                {
                    'v': [sim._v[row]],
                    'm': [sim._m[row]],
                    'n': [sim._n[row]],
                    'h': [sim._h[row]]
                }
            )
        )
    return pd.concat(spiking_histories)

# find median spiking histories
def get_median_history_from_vecs(df):
    _v = standarize_column(np.array(df['v']))
    _m = standarize_column(np.array(df['m']))
    _n = standarize_column(np.array(df['n']))
    _h = standarize_column(np.array(df['h']))

    # calculate the median of each state variable
    median_values = {
        'v': np.median(_v),
        'm': np.median(_m),
        'n': np.median(_n),
        'h': np.median(_h)
    }

    dists = []
    for i in range(len(_v)):
        dists.append(dist({'v': _v[i], 'm': _m[i], 'n': _n[i], 'h': _h[i]}, median_values))

    return {
        'v': df['v'].iloc[np.argmin(dists)],
        'm': df['m'].iloc[np.argmin(dists)],
        'n': df['n'].iloc[np.argmin(dists)],
        'h': df['h'].iloc[np.argmin(dists)]
    }

spiking_histories = {
    'base':isolate_spiking_histories(simulations['base']),
    'lw':isolate_spiking_histories(simulations['lw']),
    'lt':isolate_spiking_histories(simulations['lt']),
    'lwlt':isolate_spiking_histories(simulations['lwlt']),
    'burst':isolate_spiking_histories(simulations['burst'])
}

median_spiking_histories = {
    'base':get_median_history_from_vecs(spiking_histories['base']),
    'lw':get_median_history_from_vecs(spiking_histories['lw']),
    'lt':get_median_history_from_vecs(spiking_histories['lt']),
    'lwlt':get_median_history_from_vecs(spiking_histories['lwlt']),
    'burst':get_median_history_from_vecs(spiking_histories['burst'])
}

print('writing results to file')
for stim_type in simulations:
    # write the spike times to file
    with open(f'{data_dir}spikes_{stim_type}.txt', 'w') as fout:
        for spike in list(simulations[stim_type].spike_times):
            fout.write(f'{spike}\n')
    # write the state variables to file
    state_vars = np.array(
        (
            simulations[stim_type]._t,
            simulations[stim_type]._v,
            simulations[stim_type]._m,
            simulations[stim_type]._h,
            simulations[stim_type]._n
        )
    )
    np.save(f'{data_dir}state_vars_{stim_type}.npy', state_vars)
    # write the median spiking history to file
    with open(f'{data_dir}median_spiking_history_{stim_type}.json', 'w') as fout:
        fout.write(json.dumps(median_spiking_histories[stim_type]))

########################################################################################################################
# Wang Buzsaki model

def dist(p1, p2):
    # get distance between 2 standardized histories
    return np.sqrt(
        pow(p1['v'] - p2['v'], 2) + pow(p1['m'] - p2['m'], 2) + pow(p1['h'] - p2['h'], 2))

def isolate_spiking_histories(sim):
    spiking_histories = []
    for spike in sim.spike_times:
        row = round(40 * spike)
        spiking_histories.append(
            pd.DataFrame(
                {
                    'v': [sim._v[row]],
                    'm': [sim._m_kdr[row]],
                    'h': [sim._h_naf[row]]
                }
            )
        )
    return pd.concat(spiking_histories)

# find median spiking histories
def get_median_history_from_vecs(df):
    _v = standarize_column(np.array(df['v']))
    _m = standarize_column(np.array(df['m']))
    _h = standarize_column(np.array(df['h']))

    # calculate the median of each state variable
    median_values = {
        'v': np.median(_v),
        'm': np.median(_m),
        'h': np.median(_h)
    }

    dists = []
    for i in range(len(_v)):
        dists.append(dist({'v': _v[i], 'm': _m[i], 'h': _h[i]}, median_values))

    return {
        'v': df['v'].iloc[np.argmin(dists)],
        'm': df['m'].iloc[np.argmin(dists)],
        'h': df['h'].iloc[np.argmin(dists)]
    }

print('now simulating Wang Buzsaki model')
stim_types = ['wb']
simulations = {
    'wb':WB.WB(),
}

for stim_type in simulations:
    simulations[stim_type].add_custom_stimulus(stim_scaffold[stim_type]['ex'])
    simulations[stim_type].add_custom_stimulus(stim_scaffold[stim_type]['in'])

print('running simulations')
h.celsius = 37 ###################### change temperature for WB model
h.finitialize(-65)
h.continuerun(sim_length * ms)

print('extracting histories')
spiking_histories = {
    'wb':isolate_spiking_histories(simulations['wb']),
}

median_spiking_histories = {
    'wb':get_median_history_from_vecs(spiking_histories['wb']),
}

print('writing results to file')
for stim_type in simulations:
    # write the spike times to file
    with open(f'{data_dir}spikes_{stim_type}.txt', 'w') as fout:
        for spike in list(simulations[stim_type].spike_times):
            fout.write(f'{spike}\n')
    # write the state variables to file
    state_vars = np.array(
        (
            simulations[stim_type]._t,
            simulations[stim_type]._v,
            simulations[stim_type]._m_kdr,
            simulations[stim_type]._h_naf,
        )
    )
    np.save(f'{data_dir}state_vars_{stim_type}.npy', state_vars)
    # write the median spiking history to file
    with open(f'{data_dir}median_spiking_history_{stim_type}.json', 'w') as fout:
        fout.write(json.dumps(median_spiking_histories[stim_type]))