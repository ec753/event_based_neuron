import numpy as np
import os

from neuron import h
from neuron.units import mV, ms
h.load_file("stdrun.hoc")
h.load_file("stdlib.hoc")
h.load_file("import3d.hoc")

import json

import sys
sys.path.insert(1, "../../utils/")
import Stimuli, Pyr

import argparse

parser = argparse.ArgumentParser(description='Args')
parser.add_argument('stim_locs_file', type=str, help='path of file with stimuli locations, made with initialize_stimuli_locs.py, aka segment arrays')
parser.add_argument('n', type=int, help='number of histories to generate')
parser.add_argument('duration', type=float, help='duration')
parser.add_argument('outdir', type=str, help='directory to dump histories to')
parser.add_argument('id', type=str, help='segment array id (segment_array_8.2Hz_ID16.npy should have id = 16)')
args = parser.parse_args()

stim_locs_file = args.stim_locs_file
n = args.n
duration = args.duration
outdir = args.outdir
_id = args.id

def save_history(pyr, outdir, i, _id):
    filepath = f'{outdir}history_{i}_ID{_id}.json'
    #print(f'spike! {i}, {h.t}, {_id}')
    state_vars = pyr.all_state_vars()
    with open(filepath, "w") as outfile:
        json.dump(state_vars, outfile)

print('loading stimuli')
stim_params = Stimuli.ExperimentalStimParams()
stim_scaffold = stim_params.stim_scaffold['pyr']

stim_locs = np.load(stim_locs_file)

stimuli = Stimuli.MorphoStimuli(
    f'stimset',
    stim_scaffold['stim_type_array'],
    stim_locs, stim_scaffold,
    duration
)
print(stimuli.stimuli[0].event_times)

print('initializing cell')
pyr = Pyr.Pyr()
pyr.add_stimuli(stimuli)

nc_spike_history = h.NetCon(pyr.cell.axon(0.5)._ref_v, None, sec=pyr.cell.axon)
nc_spike_history.threshold = 0
nc_spike_history.record(lambda: save_history(pyr, f'{outdir}spiking_histories/', len(pyr.spike_times), _id))


print('setting up CVode event triggers')
h.celsius = 35
h.finitialize()

histories_times = np.sort(np.random.uniform(0, duration, n))

cvode_events = []
for i, history_time in enumerate(histories_times):
    cvode_events.append(h.CVode().event(history_time, (lambda i: lambda: save_history(pyr, f'{outdir}random_histories/', i, _id))(i)))

print('running simulation')
h.continuerun(duration * ms)
print('simulation ended')

print('class spikes', list(pyr.spike_times))
