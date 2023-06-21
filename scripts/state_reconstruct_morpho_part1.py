import numpy as np
import plotly
import matplotlib.pyplot as plt
from matplotlib import cm
import queue
import json
import gc
import os

from neuron import h
from neuron.units import mV, ms
h.load_file("stdrun.hoc")
h.load_file("stdlib.hoc")
h.load_file("import3d.hoc")
h.load_file("stdrun.hoc")

# part 1 of the state reconstruction experiment for morphologically detailed neuron,
# generates the origin simulation data for which to reconstruct

def event_type2color(event_type):
    if event_type == 'e':
        return 'red'
    elif event_type == 'i':
        return 'blue'
    elif event_type == 'o':
        return 'green'
    else:
        return 'magenta'


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
    :param stimuli: stimuli generated from poisson_times_from_stim_params
    :param max_time:
    :return:
    '''
    pq = queue.PriorityQueue()
    for seg_ind in stimuli:
        for t in stimuli[seg_ind].event_times:
            pq.put(Event(
                'stim', t, stimuli[seg_ind].tau, stimuli[seg_ind].rev_potential, seg_ind, stimuli[seg_ind].weight)
            )
    return pq


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

    def write2file(self, path):
        stimuli_data = {
            '_id': self._id,
            'rev_potential': self.rev_potential,
            'max_time': self.max_time,
            'interval': self.interval,
            'weight': self.weight,
            'delay': self.delay,
            'tau': self.tau,
            'start': self.start,
            'number': self.number,
            'event_times': self.event_times
        }

        with open(path, 'w') as fout:
            fout.write(json.dumps(stimuli_data))


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


class Pyramidal:
    def __init__(self, record_spiking_histories=False):
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
                self.all_input_segments.extend([seg for seg in part])
        self._clear_cell(record_spiking_histories)

    def _clear_cell(self, record_spiking_histories):
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

        self.v = [h.Vector().record(seg._ref_v) for sec in self.all for seg in sec]
        self.hh_secs = [sec for sec in self.all if 'hh' in sec.psection()['density_mechs']]

        '''
        self.m = [h.Vector().record(seg.hh._ref_m) for sec in hh_secs for seg in sec]
        self.h = [h.Vector().record(seg.hh._ref_h) for sec in hh_secs for seg in sec]
        self.n = [h.Vector().record(seg.hh._ref_n) for sec in hh_secs for seg in sec]
        '''

        self.spike_detector = h.NetCon(self.axon[0](0.5)._ref_v, None, sec=self.axon[0])
        self.spike_times = h.Vector()
        self.spike_detector.record(self.spike_times)

        if record_spiking_histories:
            self.spiking_histories = []
            self.spike_detector2 = h.NetCon(self.axon[0](0.5)._ref_v, None, sec=self.axon[0])
            self.spike_detector2.record(self.save)

    def __repr__(self):
        return "pyr"

    def get_state(self):
        return {
            "v": [seg.v for sec in self.all for seg in sec],
            "m": [seg.hh.m for sec in self.hh_secs for seg in sec],
            "h": [seg.hh.h for sec in self.hh_secs for seg in sec],
            "n": [seg.hh.n for sec in self.hh_secs for seg in sec]}

    def save(self):
        self.spiking_histories.append(self.get_state())

    def set_initialize_state(self, state):
        self._initial_state = state
        self.fih = h.FInitializeHandler(self._do_initial)

    def _do_initial(self):
        # state: state dict from self.get_state()
        all_segs = [seg for sec in self.all for seg in sec]
        hh_segs = [seg for sec in self.hh_secs for seg in sec]
        for seg, v in zip(all_segs, self._initial_state["v"]):
            seg.v = v
        for seg, m, h, n in zip(hh_segs, self._initial_state["m"], self._initial_state["h"], self._initial_state["n"]):
            seg.hh.m = m
            seg.hh.n = n
            seg.hh.h = h

    def load_morphology(self):
        cell = h.Import3d_SWC_read()
        cell.input("./resources/neuron_nmo/amaral/CNG version/c91662.CNG.swc")
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

    def load_stimuli_from_file(self, stimuli_file):
        with open(stimuli_file, 'r') as fin:
            stimuli_json = json.load(fin)
        for seg_ind in stimuli_json:
            stimuli = Poisson_Times(
                stimuli_json[seg_ind]['stim_type'],
                stimuli_json[seg_ind]['tau'],
                stimuli_json[seg_ind]['interval'],
                stimuli_json[seg_ind]['weight'],
                stimuli_json[seg_ind]['rev_potential'],
                event_times=stimuli_json[seg_ind]['event_times']
            )
            self.connect_input(stimuli, self.all_input_segments[int(seg_ind)])

# run 100 of these, each is initialized with a unique set of stimuli placements
# only consider those cells with above a certain spike rate

outdir = './data/state_reconstruct_morpho/original_simulation_data/'
n = 22
while n < 100:
    print(f'working on cell #{n}')
    pyr = Pyramidal(record_spiking_histories=True)
    max_time = 5000 # any longer than 10000 is a bit fraught, there are lots of state variables to keep track of

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

    stimuli = poisson_times_from_stim_params(stim_params, max_time=max_time)
    for seg in stimuli:
        pyr.connect_input(stimuli[seg], pyr.all_input_segments[seg])

    h.finitialize(-65)
    h.continuerun(max_time)

    print(f'number of spikes: {len(pyr.spike_times)}')
    if len(pyr.spike_times) > 20:
        # commit spike times for reconstruction
        spikes = list(pyr.spike_times)

        # commit membrane voltage for reconstruction
        obv_v = np.array([list(vec) for vec in pyr.v])
        print(f'array size:{obv_v.shape}')

        # write the stimuli placements
        os.mkdir(f'{outdir}stimuli_{n}')
        for seg_ind in stimuli:
            path = f'{outdir}stimuli_{n}/stimulus_{n}.{seg_ind}.json'
            stimuli[seg_ind].write2file(path)

        # write spikes to file
        with open(f'{outdir}spikes_{n}.txt', 'w') as fout:
            for t in spikes:
                fout.write(f'{t}\n')

        # write state vars to file
        np.save(f'{outdir}state_vars_{n}.npy', obv_v)
        obv_v = None
        n += 1
    pyr = None
    stimuli = None
