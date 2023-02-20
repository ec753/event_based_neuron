import sys
import json
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(1, "./utils/")
import HH, Stimuli
from neuron import h
h.load_file("stdrun.hoc")
from neuron.units import mV, ms

########## HYPERPARAMETERS ##########
parser = argparse.ArgumentParser(description='Args')
parser.add_argument('n', type=int, help='directory to dump the results to')
args = parser.parse_args()
n = args.n


data_dir = './data/partial_history/'
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

histories_base = np.load(f'{data_dir}histories_base.npy')
histories_lw = np.load(f'{data_dir}histories_lw.npy')
histories_lt = np.load(f'{data_dir}histories_lt.npy')
histories_lwlt = np.load(f'{data_dir}histories_lwlt.npy')
histories_burst = np.load(f'{data_dir}histories_burst.npy')
histories_sets = {
    'base': histories_base,
    'lw': histories_lw,
    'lt': histories_lt,
    'lwlt': histories_lwlt,
    'burst': histories_burst
}

########## EXPERIMENT ##########
print('starting experiment')

# stim scaffold is used to dynamically generate stim objects for the simulation
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

            cells[stim_type][history_ind] = HH.HH()
            stim_scaffold[stim_type]['ex'].stim_times = _e_times
            stim_scaffold[stim_type]['in'].stim_times = _i_times
            cells[stim_type][history_ind].add_custom_stimulus(stim_scaffold[stim_type]['ex'])
            cells[stim_type][history_ind].add_custom_stimulus(stim_scaffold[stim_type]['in'])
            cells[stim_type][history_ind].sim_init(
                v0=history[0],
                m0=history[1],
                h0=history[2],
                n0=history[3]
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
