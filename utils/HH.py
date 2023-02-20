from neuron.units import mV, ms
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from neuron import h
h.load_file("stdrun.hoc")

import Stimuli

class HH:
    def __init__(self):
        # set up simulation
        self.axon = h.Section(name='axon')
        self.axon.insert(h.hh)

        self.axon.L = 10
        self.axon.diam = 10

        # store stimuli
        self.stim_objects = [] # hold the stimuli objects (from stimuli.py) here
        self.syns = []  # synapses
        self.syn_currents = []  # synapse recordings
        self.stims = []  # stimuli
        self.all_stim_times = []  # stim times recording
        self.netcons = []  # net connections

        # setup simulation recording
        self._t = h.Vector().record(h._ref_t, sec=self.axon)
        self._v = h.Vector().record(self.axon(0.5)._ref_v)
        self._m = h.Vector().record(self.axon(0.5).hh._ref_m)
        self._n = h.Vector().record(self.axon(0.5).hh._ref_n)
        self._h = h.Vector().record(self.axon(0.5).hh._ref_h)
        self.spike_times = h.Vector()
        self.nc_self = h.NetCon(self.axon(0.5)._ref_v, None, sec=self.axon)
        self.nc_self.threshold = 0
        self.nc_self.record(self.spike_times)

    def add_custom_stimulus(self, stimuli):
        # stimuli: PoissonStim class object from Stimuli.py

        # add synapse
        syn = h.ExpSyn(self.axon(0))
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

    def sim_init(self, v0, m0, h0, n0):
        # print(f'sim_init: {v0}, {m0}, {h0}, {n0}')
        # initialize simulations with new initial conditions and custom stimuli
        self.v0 = v0
        self.m0 = m0
        self.h0 = h0
        self.n0 = n0

    def do_sim_init(self):
        #print(f'do_sim_init: {self.v0}, {self.m0}, {self.h0}, {self.n0}')
        for seg in self.axon:
            seg.v = self.v0
            seg.hh.m = self.m0
            seg.hh.h = self.h0
            seg.hh.n = self.n0

    def run_simulation(self, sim_length):
        fih = h.FInitializeHandler(self.do_sim_init)
        h.finitialize(-65)
        h.continuerun(sim_length * ms)

    def add_poisson_stimulus(self, stim_interval, reversal_potential, weight, tau):
        # add synapse
        syn = h.ExpSyn(self.axon(0))
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

    def plot_raster(self, start_t, stop_t):
        # stims: list of stimuli objects from stimuli.py
        fig, axes = plt.subplots(3, 1, figsize=(10, 6), sharex=True, gridspec_kw={'height_ratios': [1, 3, 1]})

        for i, stim in enumerate(self.stim_objects):
            axes[0].vlines(list(stim.stim_times), i, i + 1, color=stim.color)
        axes[0].set_yticks(np.arange(.5, len(self.stim_objects) + .5))
        axes[0].set_yticklabels([stim.name for stim in self.stim_objects])
        axes[0].set_ylabel('stimuli')
        axes[1].plot(self._t, self._v)
        axes[1].set_ylabel('membrane\nvoltage (mV)')
        axes[2].vlines(list(self.spike_times), 0, 1, color='green')
        axes[2].set_xlim(start_t, stop_t)
        axes[2].set_yticks([])
        axes[2].set_ylabel('output\nspikes')
        axes[2].set_xlabel('time (ms)')
        plt.show()

def run_poisson_sim(stim_params, history=None, sim_length=10000):
    # stim_params: list of Stimuli.PoissonStim class objects
    # initiate simulation
    sim = HH()

    if not history:
        history = {
            'v': -65.0,
            'm': 0.05293248525724958,
            'n': 0.3176769140606974,
            'h': 0.5961207535084603
        }

    for stim_param_set in stim_params:
        sim.add_poisson_stimulus(
            stim_interval=stim_param_set.interval,
            reversal_potential=stim_param_set.rev_potential,
            weight=stim_param_set.weight,
            tau=stim_param_set.tau
        )
    # add history
    sim.sim_init(
        v0=history['v'],
        m0=history['m'],
        h0=history['h'],
        n0=history['n']
    )
    # run simulation
    sim.run_simulation(sim_length=sim_length)
    spikes = np.array(sim.spike_times)

    df = {
        't': list(sim._t),
        'v': list(sim._v),
        'h': list(sim._h),
        'n': list(sim._n),
        'm': list(sim._m)
    }
    return df, spikes, sim.all_stim_times

def shift_times(event_times, shift):
    # shifts event times from by the shift amount
    return [event_time + shift for event_time in event_times]

def run_event_sim(events, history, e_w=.2, e_t=2, e_rp=0, i_w=.5, i_t=6, i_rp=-80, duration=20, robust=False):
    # arguments:
    # events: list of tuples where 0th index has 'event_type':{'e','i','o'} 1st index has 'event_time':(-inf:0]
        # in the case of nInputs.py, the events are all real-valued non-positive times before the current time t=0
    # history: dict with {'v0','m0','h0','n0'}
    # duration: time past t0 for which to continue the simulation
    # robust: False -> returns list of spikes, True -> returns list of spikes and df

    # shift is used to move the times from negative (conceptual model) to positive (NEURON simulation) and back
    shift = -min([event_time for (event_type, event_time) in events])

    # initiate simulation
    sim = HH()

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
        h0 = history['h'],
        n0 = history['n']
    )
    # run simulation
    sim.run_simulation(sim_length=shift + duration)
    spikes = list(sim.spike_times)
    # shift spikes back
    spikes = shift_times(spikes, -shift)
    if robust:
        return {
            't': list(sim._t),
            'h': list(sim._h),
            'm': list(sim._m),
            'v': list(sim._v),
            'n': list(sim._n)
        }, spikes
    else:
        return spikes