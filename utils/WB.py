import numpy as np

import numpy as np
import matplotlib.pyplot as plt

#from neuron import h, gui
from neuron import h
h.load_file("stdrun.hoc")
from neuron.units import mV, ms

import sys
import Stimuli

ex_interval = 5
ex_weight = 0.00003

in_interval = 15
in_weight = 0.00005

class WB:
    def __init__(self):
        self.soma = h.Section()

        # initialize the soma's parameters
        self.soma.L = 3.1831
        self.soma.diam = 10
        self.soma.insert(h.pas)
        self.soma.insert(h.kdr)
        self.soma.insert(h.naf)
        self.soma.g_pas = 0.0001
        self.soma.e_pas = -65
        self.soma.gmax_kdr = 0.009
        self.soma.gmax_naf = 0.035

        # store stimuli
        self.stim_objects = []
        self.syns = []
        self.syn_currents = []
        self.stims = []
        self.all_stim_times = []  # stim times recording
        self.netcons = []

        # setup simulation recording
        self._t = h.Vector().record(h._ref_t, sec=self.soma)
        self._v = h.Vector().record(self.soma(0.5)._ref_v)
        self._m_kdr = h.Vector().record(self.soma(0.5).kdr._ref_m)
        self._h_kdr = h.Vector().record(self.soma(0.5).kdr._ref_h)
        self._h_naf = h.Vector().record(self.soma(0.5).naf._ref_h)
        self.state_vars = [self._v, self._m_kdr, self._h_naf]

        self.spike_times = h.Vector()
        self.nc_self = h.NetCon(self.soma(0.5)._ref_v, None, sec=self.soma)
        self.nc_self.threshold = 0
        self.nc_self.record(self.spike_times)

        # initial conditions
        self.v0 = None
        self.m0 = None
        self.h0 = None
        self.n0 = None

    def add_custom_stimulus(self, stimuli):
        # stimuli: PoissonStim class object from Stimuli.py

        # add synapse
        syn = h.ExpSyn(self.soma(0))
        syn.tau = stimuli.tau
        syn.e = stimuli.rev_potential * mV
        syn_current = h.Vector().record(syn._ref_i)

        self.syns.append(syn)
        self.syn_currents.append(syn_current)

        netstims = [h.NetStim() for stim_time in stimuli.stim_times]
        for netstim, stim_time in zip(netstims, stimuli.stim_times):
            netstim.number = 1
            netstim.start = stim_time
            netcon = h.NetCon(netstim, syn)
            netcon.weight[0] = stimuli.weight
            netcon.delay = 0 * ms

            self.netcons.append(netcon)
        self.stims.extend(netstims)
        # don't need to record stim times as we know when they are happening already
        self.stim_objects.append(stimuli)

    def add_poisson_stimulus(self, stim_interval, reversal_potential, weight, tau):
        # add synapse
        syn = h.ExpSyn(self.soma(0))
        syn.tau = tau
        syn.e = reversal_potential * mV
        syn_current = h.Vector().record(syn._ref_i)

        self.syns.append(syn)
        self.syn_currents.append(syn_current)

        # add stimulus
        stim = h.NetStim()
        stim.number = 9999999
        stim.interval = stim_interval * ms
        stim.noise = True
        stim.start = 0 * ms
        stim_times = h.Vector()

        self.stims.append(stim)
        self.all_stim_times.append(stim_times)

        # connect stimulus #1 (excitatory) to synapse
        nc = h.NetCon(stim, syn)
        nc.delay = 0 * ms
        nc.weight[0] = weight
        nc.record(stim_times)

        self.netcons.append(nc)

    def sim_init(self, v0, m0, h0):
        # initialize simulations with new initial conditions and custom stimuli
        self.v0 = v0
        self._m_kdr0 = m0
        self._h_naf0 = h0

    def do_sim_init(self):
        #print('doing sim init')
        for seg in self.soma:
            seg.v = self.v0
            seg.kdr.m = self._m_kdr0
            seg.naf.h = self._h_naf0
            #print(seg.v, seg.kdr.m, seg.naf.h)
        #print('done with sim init')

    def run_simulation(self, sim_length):
        if self.v0:
            fih = h.FInitializeHandler(self.do_sim_init)
        # set the temperature to 37F (the temp for the session used in the original model's paper)
        h.celsius = 37

        h.finitialize(-65)
        h.continuerun(sim_length * ms)

def shift_times(event_times, shift):
    # shifts event times from by the shift amount
    return [event_time + shift for event_time in event_times]

def run_poisson_sim(stim_params, sim_length=10000):
    # stim_params: list of Stimuli.PoissonStim class objects
    # initiate simulation
    sim = WB()

    for stim_param_set in stim_params:
        sim.add_poisson_stimulus(
            stim_interval=stim_param_set.interval,
            reversal_potential=stim_param_set.rev_potential,
            weight=stim_param_set.weight,
            tau=stim_param_set.tau
        )

    # run simulation
    sim.run_simulation(sim_length=sim_length)
    spikes = np.array(sim.spike_times)

    df = {
        't': list(sim._t),
        'v': list(sim._v),
        'm': list(sim._m_kdr),
        'h': list(sim._h_naf),
    }
    return df, spikes, sim.all_stim_times

def run_event_sim(events, history, e_w=0.00003, e_t=2, e_rp=0, i_w=0.00005, i_t=6, i_rp=-80, duration=20, robust=False):
    # arguments:
    # events: list of tuples where 0th index has 'event_type':{'e','i','o'} 1st index has 'event_time':(-inf:0]
        # in the case of nInputs.py, the events are all real-valued non-positive times before the current time t=0
    # history: dict with {'v0','m0','h0','n0'}
    # duration: time past t0 for which to continue the simulation
    # robust: False -> returns list of spikes, True -> returns list of spikes and df

    # shift is used to move the times from negative (conceptual model) to positive (NEURON simulation) and back
    shift = -min([event_time for (event_type, event_time) in events])

    # initiate simulation
    sim = WB()

    # add excitatory_stimuli
    e_stim = Stimuli.PoissonStim(
        name='e',
        stim_id='e',
        interval='na',
        rev_potential=e_rp,
        weight=e_w,
        tau=e_t,
        seed='na',
        stim_times=shift_times([event_time for (event_type, event_time) in events if event_type == 'e'], shift)
    )
    sim.add_custom_stimulus(e_stim)
    # add inhibitory_stimuli
    i_stim = Stimuli.PoissonStim(
        name='i',
        stim_id='i',
        interval='na',
        rev_potential=i_rp,
        weight=i_w,
        tau=i_t,
        seed='na',
        stim_times=shift_times([event_time for (event_type, event_time) in events if event_type == 'i'], shift)
    )
    sim.add_custom_stimulus(i_stim)
    # add history
    sim.sim_init(
        v0 = history['v'],
        m0 = history['m'],
        h0 = history['h']
    )
    # run simulation
    sim.run_simulation(sim_length=shift + duration)
    spikes = list(sim.spike_times)
    # shift spikes back
    spikes = shift_times(spikes, -shift)
    if robust:
        return {
            't': list(sim._t),
            'v': list(sim._v),
            'm': list(sim._m_kdr),
            'h': list(sim._h_naf),
        }, spikes
    else:
        return spikes