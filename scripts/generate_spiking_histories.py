import sys

sys.path.insert(1, "../utils/")
import HH, WB, Stimuli

import math
import numpy as np

from neuron import h
h.load_file("stdrun.hoc")
from neuron.units import mV, ms


# part 1 of the state reconstruction experiment,
# generates the spiking histories

data_dir = '../data/state_reconstruct_test/'
sim_length = 1_000_000

stim_types = [
    'base',
    'lw',
    'lt',
    'lwlt',
    'burst'
]

print('generating stimuli')
e_times = Stimuli.poisson_process_duration(5, sim_length)
i_times = Stimuli.poisson_process_duration(15, sim_length)

stim_params = Stimuli.ExperimentalStimParams()
stim_scaffold = stim_params.stim_scaffold

for stim_type in stim_scaffold:
    stim_scaffold[stim_type]['ex'].stim_times = e_times
    stim_scaffold[stim_type]['in'].stim_times = i_times

print('running HH simulations')
spike_history_simulations = {
    stim_type: HH.HH() for stim_type in stim_types
}

for stim_type in stim_types:
    spike_history_simulations[stim_type].add_custom_stimulus(stim_scaffold[stim_type]['ex'])
    spike_history_simulations[stim_type].add_custom_stimulus(stim_scaffold[stim_type]['in'])

h.finitialize(-65)
h.continuerun(sim_length * ms)

print('gathering spiking histories')
spiking_histories = {stim_type:[] for stim_type in stim_types}
for stim_type in stim_types:
    _sim = spike_history_simulations[stim_type]

    for spike_time in _sim.spike_times:
        _row = math.ceil(40 * spike_time)
        spiking_histories[stim_type].append(
            [var[_row] for var in _sim.state_vars]
        )
spiking_histories = {stim_type:np.array(spiking_histories[stim_type]) for stim_type in stim_types}

for stim_type in stim_types:
    print(f'num spiking histories {stim_type}: {spiking_histories[stim_type].shape}')

    np.save(f'{data_dir}spiking_histories_{stim_type}.npy', spiking_histories[stim_type])

# collect simulations
spike_history_simulations = None


########## Wang Buzsaki model #######################################################################################
print('running WB simulation')
spike_history_simulation_wb = WB.WB()
spike_history_simulation_wb.add_custom_stimulus(stim_scaffold['wb']['ex'])
spike_history_simulation_wb.add_custom_stimulus(stim_scaffold['wb']['in'])
h.celsius = 37
spike_history_simulation_wb.run_simulation(sim_length)

spiking_histories_wb = []
for spike_time in spike_history_simulation_wb.spike_times:
    _row = math.ceil(40 * spike_time)
    spiking_histories_wb.append(
        [var[_row] for var in spike_history_simulation_wb.state_vars]
    )
spiking_histories_wb = np.array(spiking_histories_wb)
print(f'num spiking histories wb: {spiking_histories_wb.shape}')

np.save(f'{data_dir}spiking_histories_wb.npy', spiking_histories_wb)