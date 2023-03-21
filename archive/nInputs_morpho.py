import sys
sys.path.insert(1, "./utils/")
import Stimuli, Morpho

from neuron import h
from neuron.units import mV, ms
import numpy as np
import queue
import json
import argparse


########################################################################################################################
# command line arguments
parser = argparse.ArgumentParser(description='')
parser.add_argument('outdir', type=str, help='directory to dump the results to')
parser.add_argument('exp_name', type=str, help='name of the experiment')
parser.add_argument('ninputs', type=int, help='number of inputs to test with')
parser.add_argument('duration', type=float, help='duration of each simulation')
parser.add_argument('num_excitatory_stims', type=int, help='number of excitatory synapse connections')
parser.add_argument('excitatory_interval', type=float, help='expected interval of poisson generated excitatory stimuli at each excitatory synapse')
parser.add_argument('excitatory_rev_potential', type=float, help='')
parser.add_argument('excitatory_weight', type=float, help='')
parser.add_argument('excitatory_tau', type=float, help='')
parser.add_argument('num_inhibitory_stims', type=int, help='')
parser.add_argument('inhibitory_interval', type=float, help='')
parser.add_argument('inhibitory_rev_potential', type=float, help='')
parser.add_argument('inhibitory_weight', type=float, help='')
parser.add_argument('inhibitory_tau', type=float, help='')
args = parser.parse_args()
########################################################################################################################
class Event:
    def __init__(self, _id, t, tau, rev_potential, seg_ind, weight):
        self._id = _id
        self.t = t
        self.tau = tau
        self.rev_potential = rev_potential
        self.seg_ind = seg_ind
        self.weight = weight

    def __lt__(self, other):
        return self.t < other.t

    def __repr__(self):
        return str(self._id) + str(self.t)

    def deliver(self):
        # print(self)
        return


def generate_event_queue(stimuli):
    '''
    :param stimuli:
    :return:
    '''
    pq = queue.PriorityQueue()
    for seg_ind in stimuli:
        for t in stimuli[seg_ind].event_times:
            pq.put(Event(
                'stim', t, stimuli[seg_ind].tau, stimuli[seg_ind].rev_potential, seg_ind, stimuli[seg_ind].weight)
            )
    return pq


def get_n_events(event_log, n):
    # currently ignores output spike events
    events = event_log['stimuli'][-n:]

    return events


def remove_duplicate_spikes(spikes):
    final_spikes = []
    for spike_ind in range(len(spikes) - 1):
        if (spikes[spike_ind + 1] - spikes[spike_ind]) > 1:
            final_spikes.append(spikes[spike_ind])
    final_spikes.append(spikes[-1])
    return final_spikes

########################################################################################################################
# main
########################################################################################################################
if __name__ == '__main__':
    outdir = args.outdir
    exp_name = args.exp_name
    ninputs = args.ninputs
    duration = args.duration

    num_excitatory_stims = args.num_excitatory_stims
    excitatory_interval = args.excitatory_interval
    excitatory_rev_potential = args.excitatory_rev_potential
    excitatory_weight = args.excitatory_weight
    excitatory_tau = args.excitatory_tau

    num_inhibitory_stims = args.num_inhibitory_stims
    inhibitory_interval = args.inhibitory_interval
    inhibitory_rev_potential = args.inhibitory_rev_potential
    inhibitory_weight = args.inhibitory_weight
    inhibitory_tau = args.inhibitory_tau

    # initialize cell
    pyr = Morpho.Pyramidal()

    # generate stimuli
    print('generating stimuli')

    excitatory_stimuli_set = Stimuli.PoissonStimSet(
        num_excitatory_stims,
        pyr.all_input_segments,
        excitatory_interval,
        duration,
        excitatory_rev_potential,
        excitatory_weight,
        excitatory_tau)

    inhibitory_stimuli_set = Stimuli.PoissonStimSet(
        num_inhibitory_stims,
        pyr.all_input_segments,
        inhibitory_interval,
        duration,
        inhibitory_rev_potential,
        inhibitory_weight,
        inhibitory_tau)

    # write stimuli to file
    excitatory_stimuli_set.write_to_file(f'{outdir}/{exp_name}_excitatory_stimuli.json')
    inhibitory_stimuli_set.write_to_file(f'{outdir}/{exp_name}_inhibitory_stimuli.json')

    # run comparison morpho model
    for stim in excitatory_stimuli_set.stimuli:
        pyr.connect_input(stim, pyr.all_input_segments[stim.stim_id])

    h.finitialize(-65)
    h.continuerun(max_time)

    # write observed spike to file
    print('number of observed spikes:', len(list(pyr.spike_times)))
    with open(f'{outdir}/{exp_name}_obv_spikes.csv', 'w') as fout:
        for spike in list(pyr.spike_times):
            fout.write(str(spike) + '\n')

    # performing experiments with n inputs
    print(f'experimenting with {n} inputs')
    stim_queue = generate_event_queue(stimuli)

    event_log = {
        'stimuli': [],  # stores stimuli Event class objects
        'output_spikes': []  # stores stimuli Event class objects
    }

    while True:
        try:
            event = stim_queue.get_nowait()
            stim_queue.task_done()

            # add stimulus to log
            event_log['stimuli'].append(event)
            # generate new behavior
            events = get_n_events(event_log, n)
            nst = event_sim(events)

            print('queue size:', stim_queue.qsize())
            if nst:
                #print('nsts:', nst)
                event_log['output_spikes'].append(nst)

        except queue.Empty:
            break

    if len(event_log['output_spikes']) > 0:
        n_inputs_spikes = remove_duplicate_spikes(event_log['output_spikes'])

        # write results to file
        with open(f'{outdir}/{exp_name}_{n}_rep_spikes.csv', 'w') as fout:
            for spike in n_inputs_spikes:
                fout.write(str(spike) + '\n')