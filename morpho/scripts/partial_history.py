import json
import numpy as np
import os

from neuron import h
from neuron.units import mV, ms
h.load_file("stdrun.hoc")
h.load_file("stdlib.hoc")
h.load_file("import3d.hoc")

import sys
sys.path.insert(1, "../../utils/")
import Stimuli, Pyr

# ns x histories x  input_patterns

########## HYPERPARAMETERS ##########
import argparse
parser = argparse.ArgumentParser(description='Args')
parser.add_argument('segment_arrayID', type=str, help='ex: "ID2"')
parser.add_argument('n', type=int, help='n as in n inputs')
parser.add_argument('num_histories', type=int, help='')
parser.add_argument('num_input_patterns', type=int, help='')
parser.add_argument('data_dir', type=str, help='')
args = parser.parse_args()

segment_arrayID = args.segment_arrayID
n = args.n
num_histories = args.num_histories
num_input_patterns_per_n = args.num_input_patterns
data_dir = args.data_dir

########## STIMULI ##########
print('generating stimuli')
stim_locs_file = [file for file in os.listdir(f'{data_dir}segment_arrays/') if segment_arrayID+'.npy' in file][0]
print(stim_locs_file)

stim_params = Stimuli.ExperimentalStimParams()
stim_scaffold = stim_params.stim_scaffold['pyr']
stim_locs = np.load(f'{data_dir}segment_arrays/{stim_locs_file}')

stimuli_patterns = {}

for pattern_ind in range(num_input_patterns_per_n):
    stimuli_patterns[pattern_ind] = [
        Stimuli.poisson_process_n(stim_scaffold[stim_type].interval, n) for stim_type in stim_scaffold['stim_type_array']
    ]

with open(data_dir + f"stimuli_pattern_{n}.json", "w") as fout:
    fout.write(json.dumps(stimuli_patterns))

########## HISTORIES ##########
histories_files = [file for file in os.listdir(f'{data_dir}random_histories/') if segment_arrayID+'.json' in file]
histories = []
for history_file in histories_files[:num_histories]:
    with open(f'{data_dir}random_histories/{history_file}') as fin:
        histories.append(json.load(fin))

########## EXPERIMENT ##########
for pattern_ind in range(num_input_patterns_per_n):
    print(f'{pattern_ind}/{num_input_patterns_per_n}')
    results = []
    print('setting up stimuli')
    stimuli_pattern = stimuli_patterns[pattern_ind]
    last_stimulus = max([item for row in stimuli_pattern for item in row]) # used instead of recentering
    stimuli = Stimuli.MorphoStimuli(
        f'stimset',
        stim_scaffold['stim_type_array'],
        stim_locs, stim_scaffold,
        last_stimulus
    )
    for stimuli_pattern_at_loc, stimulus in zip(stimuli_pattern, stimuli.stimuli):
        stimulus.event_times = stimuli_pattern_at_loc
    cells = {}
    print('generating cells')
    for history_ind, history in enumerate(histories):
        cells[history_ind] = Pyr.Pyr()
        # initialize history
        cells[history_ind].initialize_state_vars(history)
        # connect stimuli
        cells[history_ind].add_stimuli(stimuli)
    
    print('running simulation')
    h.celsius = 35
    h.finitialize()
    h.continuerun(last_stimulus + 50 * ms)
    
    print('parsing nsts')
    for history_ind in range(len(histories)):
        nsts = [spike - last_stimulus for spike in list(cells[history_ind].spike_times)]
        nsts = [nst for nst in nsts if nst > 0]
        if len(nsts) < 1:
            results.append(np.nan)
        else:
            results.append(min(nsts))

    np.save(f'{data_dir}partial_history/{segment_arrayID}_{n}_{pattern_ind}', np.array(results))