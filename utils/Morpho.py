from neuron import h
from neuron.units import mV, ms
import numpy as np
import queue
import json

h.load_file("stdrun.hoc")
h.load_file("stdlib.hoc")
h.load_file("import3d.hoc")


class Pyramidal:
    def __init__(self, path2morpho, record_spiking_histories=False):
        self.load_morphology(path2morpho)
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

    def load_morphology(self, path2morph):
        cell = h.Import3d_SWC_read()
        cell.input(path2morph)
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