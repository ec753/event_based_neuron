from neuron import h
from neuron.units import mV, ms
import numpy as np
import queue
import json
import argparse

h.load_file("stdrun.hoc")
h.load_file("stdlib.hoc")
h.load_file("import3d.hoc")
h.load_file("stdrun.hoc")

########################################################################################################################
# arguments
########################################################################################################################
parser = argparse.ArgumentParser(description='Args')
parser.add_argument('outdir', type=str, help='directory to dump the results to')
parser.add_argument('exp_name', type=str, help='name of the experiment')
args = parser.parse_args()

########################################################################################################################
# generate stimuli times
########################################################################################################################
class Poisson_Times:
    def __init__(self, _id, tau, interval, weight, rev_potential, event_times=None, max_time=1000000, number=99999999,
                 delay=0, start=0):
        '''
        :param _id:
        :param event_times: instead of auto generating, provide a list of event_times
        :param max_time: maximum time (simulation duration)
        :param number: maximum number of stimuli (typically inconsequential if max_time is reasonable)
        '''

        self._id = _id
        self.rev_potential = rev_potential
        self.max_time = max_time
        self.interval = interval
        self.weight = weight
        self.delay = delay
        self.tau = tau
        self.start = start
        self.number = number
        self.event_times = []

        if event_times:
            # load event times
            self.event_times = event_times
        else:
            # generate event times
            event_time = 0
            for i in range(number):
                event_time += np.random.exponential(self.interval)
                if event_time < max_time:
                    self.event_times.append(event_time)
                else:
                    break


def poisson_times_from_stim_params(stim_params, max_time):
    poisson_times = {}
    for _id in stim_params:
        for seg_ind in stim_params[_id]['seg_inds']:
            poisson_times[seg_ind] = Poisson_Times(
                _id,
                stim_params[_id]['tau'],
                stim_params[_id]['interval'],
                stim_params[_id]['weight'],
                stim_params[_id]['rev_potential'],
                max_time=max_time
            )
    return poisson_times


########################################################################################################################
# set up pyramidal cell
########################################################################################################################
class Pyramidal:
    def __init__(self):
        self.load_morphology()
        # do discretization, ion channels, etc
        for sec in self.all:
            sec.nseg = int(1 + 2 * (sec.L // 40))
        h.hh.insert(self.axon)
        h.hh.insert(self.soma)
        h.pas.insert(self.dend)  # passive leak
        h.pas.insert(self.apic)  # passive leak
        self.all_input_segments = []
        for morph in [self.apic, self.dend]:
            for part in morph:
                # self.all_input_segments.append(part)
                self.all_input_segments.extend([seg for seg in part.allseg()])
        # storing input mechanisms
        self.syns = []
        self.net_stims = []
        self.netcons = []
        self.stims = []
        # recording
        self.v_apic = h.Vector().record(self.apic[100](0.5)._ref_v)
        self.v_soma = h.Vector().record(self.soma[0](0.5)._ref_v)
        self.v_axon = h.Vector().record(self.axon[0](0.5)._ref_v)
        self._t = h.Vector().record(h._ref_t)
        self.spike_detector = h.NetCon(self.axon[0](0.5)._ref_v, None, sec=self.axon[0])
        self.spike_times = h.Vector()
        self.spike_detector.record(self.spike_times)

    def __repr__(self):
        return "pyr"

    def load_morphology(self):
        cell = h.Import3d_SWC_read()
        cell.input("./neuron_nmo/amaral/CNG version/c91662.CNG.swc")
        i3d = h.Import3d_GUI(cell, False)
        i3d.instantiate(self)

    def connect_input(self, stimuli, seg):
        '''
        :param stimuli: Poisson_Times class object
        :param seg: NEURON simulation segment
        :return:
        '''
        syn = h.ExpSyn(seg)
        syn.tau = stimuli.tau
        syn.e = stimuli.rev_potential

        vec_stim_times = h.Vector(stimuli.event_times)
        vec_stim = h.VecStim()
        vec_stim.play(vec_stim_times)

        nc = h.NetCon(vec_stim, syn)
        nc.weight[0] = 1  # stimuli.weight
        nc.delay = stimuli.delay

        self.syns.append(syn)
        self.netcons.append(nc)

        netstims = [h.NetStim() for stim_time in stimuli.event_times]
        for netstim, event_time in zip(netstims, stimuli.event_times):
            netstim.number = 1
            netstim.start = event_time
            netcon = h.NetCon(netstim, syn)
            netcon.weight[0] = stimuli.weight
            netcon.delay = 0 * ms

            self.netcons.append(netcon)
        self.stims.extend(netstims)


def event_sim(events):
    '''
    # used for simulating a morpho cell, detatched from other simulations, for n inputs
    :param events:
    :return:
    '''
    pyr = Pyramidal()

    # generate necessary synapses
    syns = {}
    for event in events:
        syns[event.seg_ind] = h.ExpSyn(pyr.all_input_segments[event.seg_ind])
        syns[event.seg_ind].tau = event.tau
        syns[event.seg_ind].e = event.rev_potential

    # create net connections for each stimulus
    min_event_time = min([event.t for event in events])
    max_event_time = max([event.t for event in events])

    netstims = [h.NetStim() for event in events]
    for netstim, event in zip(netstims, events):
        netstim.number = 1
        netstim.start = event.t - min_event_time
        netcon = h.NetCon(netstim, syns[event.seg_ind])
        netcon.weight[0] = event.weight
        netcon.delay = 0 * ms
        pyr.netcons.append(netcon)

    # run simulation
    h.finitialize(-65)
    h.continuerun(max_event_time - min_event_time + 20)
    nsts = [spike + min_event_time for spike in list(pyr.spike_times)]
    nsts = [spike for spike in nsts if spike > max_event_time]
    if len(nsts) > 0:
        return nsts[0]
    else:
        return None


########################################################################################################################
# priority queue
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
    # generate stimuli
    print('generating stimuli')

    # initialize cell
    pyr = Pyramidal()

    stim_params = {
        'e': {
            'n_stim_sets': 10,
            'tau': 2,
            'interval': 25,
            'weight': .25,
            'rev_potential': 0,
            'seg_inds': np.random.randint(0, len(pyr.all_input_segments), 10)
        },
        'i': {
            'n_stim_sets': 5,
            'tau': 6,
            'interval': 25,
            'weight': .25,
            'rev_potential': -80,
            'seg_inds': np.random.randint(0, len(pyr.all_input_segments), 5)
        }
    }

    # generate stimuli
    max_time = 10000
    stimuli = poisson_times_from_stim_params(stim_params, max_time=max_time)

    # write stimuli to file
    stimuli_2_file = {
        int(seg_ind):
            {
                'stim_type': stimuli[seg_ind]._id,
                'rev_potential': stimuli[seg_ind].rev_potential,
                'interval': stimuli[seg_ind].interval,
                'weight': stimuli[seg_ind].weight,
                'tau': stimuli[seg_ind].tau,
                'event_times': stimuli[seg_ind].event_times
            } for seg_ind in stimuli
    }
    with open(f'{args.outdir}{args.exp_name}_stimuli.json', "w") as fout:
        json.dump(stimuli_2_file, fout)

    # run comparison morpho model
    for seg in stimuli:
        pyr.connect_input(stimuli[seg], pyr.all_input_segments[seg])

    h.finitialize(-65)
    h.continuerun(max_time)

    # write observed spike to file
    print('number of observed spikes:', len(list(pyr.spike_times)))
    with open(f'{args.outdir}{args.exp_name}_obv_spikes.csv', 'w') as fout:
        for spike in list(pyr.spike_times):
            fout.write(str(spike) + '\n')

    # initialize committed event log
    for n in range(3, 31):
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
            with open(f'{args.outdir}{args.exp_name}_{n}_rep_spikes.csv', 'w') as fout:
                for spike in n_inputs_spikes:
                    fout.write(str(spike) + '\n')
