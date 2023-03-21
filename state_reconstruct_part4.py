import sys
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
sys.path.insert(1, "./utils/")
import HH, Stimuli
from neuron import h
h.load_file("stdrun.hoc")
from neuron.units import mV, ms

# part 4 of the state reconstruction experiment,
# does the reconstructions of frames from the origin simulations, but for a longer duration than part2
origin_sim_length = 1_000_000
reconstruct_duration = 1000
num_reconstructions = 1000
stim_type = 'base'

print('loading origin data')
origin_sim_data_dir = './data/state_reconstruct/original_simulation_data/'
reconstruction_data_dir = './data/state_reconstruct/reconstruction_data/'

# e_times
with open(f'{origin_sim_data_dir}e_times.txt', 'r') as fin:
    e_times = [float(t) for t in fin.read().splitlines()]

# i_times
with open(f'{origin_sim_data_dir}i_times.txt', 'r') as fin:
    i_times = [float(t) for t in fin.read().splitlines()]

# origin spike times
with open(f'{origin_sim_data_dir}spikes_{stim_type}.txt', 'r') as fin:
    spikes = [float(spike) for spike in fin.read().splitlines()]
viable_spikes = [spike for spike in spikes[1:] if (spike < origin_sim_length - reconstruct_duration)]

# median spiking history
with open(f'{origin_sim_data_dir}median_spiking_history_{stim_type}.json', 'r') as fin:
    o_history = json.load(fin)

# origin state variables
origin_state_vars = np.load(f'{origin_sim_data_dir}state_vars_{stim_type}.npy')

print('preparing reconstruction simulations')
stim_scaffold = {
    'base': {
        'ex': Stimuli.PoissonStim(
            'ex_base', 'ex_base',
            interval=5,
            rev_potential=0,
            weight=0.0002,
            tau=2,
            seed='na'
        ),
        'in': Stimuli.PoissonStim(
            'in_base', 'in_base',
            interval=15,
            rev_potential=-80,
            weight=0.0005,
            tau=6,
            seed='na'
        )
    },
    'lw': {
        'ex': Stimuli.PoissonStim(
            'ex_lw', 'ex_lw',
            interval=5,
            rev_potential=0,
            weight=0.00015,
            tau=2,
            seed='na'
        ),
        'in': Stimuli.PoissonStim(
            'in_lw', 'in_lw',
            interval=15,
            rev_potential=-80,
            weight=0.0002,
            tau=6,
            seed='na'
        )
    },
    'lt': {
        'ex': Stimuli.PoissonStim(
            'ex_lt', 'ex_lt',
            interval=5,
            rev_potential=0,
            weight=0.0002,
            tau=10,
            seed='na'
        ),
        'in': Stimuli.PoissonStim(
            'in_lt', 'in_lt',
            interval=15,
            rev_potential=-80,
            weight=0.0005,
            tau=40,
            seed='na'
        )
    },
    'lwlt': {
        'ex': Stimuli.PoissonStim(
            'ex_lwlt', 'ex_lwlt',
            interval=5,
            rev_potential=0,
            weight=0.00015,
            tau=10,
            seed='na'
        ),
        'in': Stimuli.PoissonStim(
            'in_lwlt', 'in_lwlt',
            interval=15,
            rev_potential=-80,
            weight=0.0002,
            tau=40,
            seed='na'
        )
    },
    'burst': {
        'ex': Stimuli.PoissonStim(
            'ex_burst', 'ex_burst',
            interval=5,
            rev_potential=0,
            weight=0.0001,
            tau=40,
            seed='na'
        ),
        'in': Stimuli.PoissonStim(
            'in_burst', 'in_burst',
            interval=15,
            rev_potential=-80,
            weight=0.0005,
            tau=20,
            seed='na'
        )
    }
}

original_dfs = []
reconstruction_cells = [HH.HH() for i in range(len(viable_spikes))]
fihs = []

viable_spike_inds = np.random.choice(np.arange(0, len(viable_spikes)), num_reconstructions)

progress = 0.0
print('______PROGRESS______')

for i in range(num_reconstructions):
    cell = reconstruction_cells[i]
    starting_spike = viable_spikes[viable_spike_inds[i]]

    # find original df
    start_ind = int(starting_spike * 40)
    end_ind = start_ind + (reconstruct_duration * 40) + 1
    original_dfs.append(origin_state_vars[:, start_ind:end_ind])

    # inject stimuli
    _e_times = [
        t - starting_spike for t in e_times if (t > starting_spike) and (t < starting_spike + reconstruct_duration)
    ]
    _i_times = [
        t - starting_spike for t in i_times if (t > starting_spike) and (t < starting_spike + reconstruct_duration)
    ]

    _e_stims = Stimuli.PoissonStim(
        rev_potential=stim_scaffold[stim_type]['ex'].rev_potential,
        weight=stim_scaffold[stim_type]['ex'].weight,
        tau=stim_scaffold[stim_type]['ex'].tau,
        stim_times=_e_times,
    )

    _i_stims = Stimuli.PoissonStim(
        rev_potential=stim_scaffold[stim_type]['in'].rev_potential,
        weight=stim_scaffold[stim_type]['in'].weight,
        tau=stim_scaffold[stim_type]['in'].tau,
        stim_times=_i_times,
    )

    cell.add_custom_stimulus(_e_stims)
    cell.add_custom_stimulus(_i_stims)

    # initialize
    cell.sim_init(
        v0=o_history['v'],
        m0=o_history['m'],
        h0=o_history['h'],
        n0=o_history['n']
    )

    fihs.append(h.FInitializeHandler(cell.do_sim_init))

    if i / num_reconstructions > progress:
        print('=',end='')
        progress+=0.05
print()

print('running simulations')
h.finitialize(-65)
h.continuerun(reconstruct_duration * ms)

reconstructed_state_vars = [np.array((cell._t, cell._v, cell._m, cell._h,cell._n)) for cell in reconstruction_cells]
reconstructed_state_vars = np.array(reconstructed_state_vars)
original_dfs = np.array(original_dfs)

print('writing results to file')

np.save(f'{reconstruction_data_dir}reconstruct_state_vars_long_{stim_type}.npy', reconstructed_state_vars)
np.save(f'{reconstruction_data_dir}origin_state_vars__long_{stim_type}.npy', original_dfs)

