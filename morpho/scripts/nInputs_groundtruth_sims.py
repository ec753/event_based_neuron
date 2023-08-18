import numpy as np
import json
import os

from neuron import h
from neuron.units import mV, ms

import sys
sys.path.insert(1, "../../utils/")
import Stimuli, Pyr


duration = 10000
uniqueID = 'palmerscratch'

##### READ STIMULI #####
path2stimulifile = '../../data/morpho/nInputs_palmerscratch_stimuli/stim_times_0.json'

with open(path2stimulifile, 'r') as fin:
    stim_times = json.load(fin)

##### READ SPIKES #####
path2spikes = '../../data/morpho/nInputs_palmerscratch_spikes/'

ns = np.arange(1,11)
seg_locIDs = list(set([file.split('_')[2] for file in os.listdir(path2spikes)]))

spikes = {seg_locID:{} for seg_locID in seg_locIDs}
missing_files = []
for seg_locID in seg_locIDs:
    for n in ns:
        try:
            _spikes0 = np.load(f'{path2spikes}spikes_0_{seg_locID}_{n}.npy')
        except:
            _spikes0 = np.zeros(0)
            missing_files.append(f'spikes_0_{seg_locID}_{n}.npy')
        try:
            _spikes1 = np.load(f'{path2spikes}spikes_1_{seg_locID}_{n}.npy')
            spikes[seg_locID][n] = _spikes1
        except:
            _spikes1 = np.zeros(0)
            missing_files.append(f'spikes_1_{seg_locID}_{n}.npy')

##### SET UP SIMULATIONS #####
cells = {seg_locID : Pyr.Pyr() for seg_locID in seg_locIDs}
stimuli = {}

for seg_locID in seg_locIDs:
    print(f'setting up {seg_locID} simulation')
    path2segarrays = '../../data/morpho/segment_arrays/'
    seg_loc_file = [file for file in os.listdir(path2segarrays) if seg_locID+'.npy' in file][0]
    print(seg_loc_file)

    stim_params = Stimuli.ExperimentalStimParams()
    stim_scaffold = stim_params.stim_scaffold['pyr']
    stim_locs = np.load(f'{path2segarrays}{seg_loc_file}')

    # generate the stimuli
    stimuli[seg_locID] = Stimuli.MorphoStimuli(
        seg_locID, 
        stim_params.stim_scaffold['pyr']['stim_type_array'],
        stim_locs,
        stim_scaffold,
        duration
    )
    # set the stimuli times
    for i, stimulus in enumerate(stimuli[seg_locID].stimuli):
        stimulus.event_times = stim_times[str(i)]

    # connect the stimuli
    cells[seg_locID].add_stimuli(stimuli[seg_locID])

##### RUN SIMULATIONS #####
print('running simulations')
h.celsius = 35
h.finitialize()
h.continuerun(duration * ms)

##### SAVE RESULTS #####
print('saving results')
for seg_locID in seg_locIDs:
    np.save(f'../../data/morpho/nInputs_groundtruth_sims/groundtruth_spikes_{seg_locID}_{uniqueID}.npy', list(cells[seg_locID].spike_times))