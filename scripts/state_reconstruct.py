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
import argparse

parser = argparse.ArgumentParser(description='Args')
parser.add_argument('stim_type', type=str, help='stim_type')
args = parser.parse_args()

# part 2 of the state reconstruction experiment,
reconstruct_duration = 250
num_reconstructions = 5000
data_dir = '../data/state_reconstruct_test/'

stim_type = args.stim_type

print('loading histories')
spiking_histories = np.load(f'{data_dir}spiking_histories_{stim_type}.npy')

stim_params = Stimuli.ExperimentalStimParams()
stim_scaffold = stim_params.stim_scaffold

print('initializing simulations')
if stim_type == 'wb':
    origin_simulations = [WB.WB() for i in range(num_reconstructions)]
    reconstruct_simulations = [WB.WB() for i in range(num_reconstructions)]
else:
    origin_simulations = [HH.HH() for i in range(num_reconstructions)]
    reconstruct_simulations = [HH.HH() for i in range(num_reconstructions)]
fihs = []

for i in range(num_reconstructions):
    # stimulate with the same stimuli
    _e_times = Stimuli.poisson_process_duration(stim_scaffold[stim_type]['ex'].interval, reconstruct_duration)
    _i_times = Stimuli.poisson_process_duration(stim_scaffold[stim_type]['in'].interval, reconstruct_duration)
    _e_stims = stim_scaffold[stim_type]['ex']
    _i_stims = stim_scaffold[stim_type]['in']
    _e_stims.stim_times = _e_times
    _i_stims.stim_times = _i_times

    origin_simulations[i].add_custom_stimulus(stim_scaffold[stim_type]['ex'])
    origin_simulations[i].add_custom_stimulus(stim_scaffold[stim_type]['in'])

    reconstruct_simulations[i].add_custom_stimulus(stim_scaffold[stim_type]['ex'])
    reconstruct_simulations[i].add_custom_stimulus(stim_scaffold[stim_type]['in'])

    # inirialize the sims with random spiking histories
    history_inds = np.random.choice(spiking_histories.shape[0], 2)

    if stim_type == 'wb':
        origin_simulations[i].sim_init(
            v0=spiking_histories[history_inds[0], 0],
            m0=spiking_histories[history_inds[0], 1],
            h0=spiking_histories[history_inds[0], 2],
        )
        reconstruct_simulations[i].sim_init(
            v0=spiking_histories[history_inds[1], 0],
            m0=spiking_histories[history_inds[1], 1],
            h0=spiking_histories[history_inds[1], 2],
        )
    else:
        origin_simulations[i].sim_init(
            v0=spiking_histories[history_inds[0], 0],
            m0=spiking_histories[history_inds[0], 1],
            h0=spiking_histories[history_inds[0], 2],
            n0=spiking_histories[history_inds[0], 3],
        )
        reconstruct_simulations[i].sim_init(
            v0=spiking_histories[history_inds[1], 0],
            m0=spiking_histories[history_inds[1], 1],
            h0=spiking_histories[history_inds[1], 2],
            n0=spiking_histories[history_inds[1], 3],
        )

    # handle initialize handlers
    fihs.append(h.FInitializeHandler(origin_simulations[i].do_sim_init))
    fihs.append(h.FInitializeHandler(reconstruct_simulations[i].do_sim_init))
print('running simulations')
if stim_type == 'wb':
    h.celsius = 37
h.finitialize(-65)
h.continuerun(reconstruct_duration * ms)

print('calculating errors')
origin_v = np.array([_sim._v for _sim in origin_simulations])
reconstruct_v = np.array([_sim._v for _sim in reconstruct_simulations])

np.save(f'{data_dir}origin_v_{stim_type}.npy', origin_v)
np.save(f'{data_dir}reconstruct_v_{stim_type}.npy', reconstruct_v)


