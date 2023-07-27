import random
import numpy as np
from neuron import h

def poisson_process_n(interval, n):
    interspikes = [random.expovariate(1. / interval) for _ in range(n)]
    t = 0
    times = []
    for interspike in interspikes:
        t += interspike
        times.append(t)
    return times

def poisson_process_duration(interval, duration):
    t = random.expovariate(1. / interval)
    times = []
    while t < duration:
        times.append(t)
        t += random.expovariate(1. / interval)
    return times

def excitatory_and_inhibitory_n(ex_interval, in_interval, n):
    # provides n stimuli as a mix of excitatory and inhibitory
    ex_stimuli = [-t for t in poisson_process_n(ex_interval, n)]
    in_stimuli = [-t for t in poisson_process_n(in_interval, n)]

    stimuli = zip(['e'] * n + ['i'] * n, ex_stimuli + in_stimuli)
    stimuli = sorted(stimuli, key=lambda x: x[1])
    stimuli = stimuli[-n:]
    min_stim = min([stim[1] for stim in stimuli])

    stimuli = [(stim_type, t - min_stim) for stim_type, t in stimuli]
    return stimuli

class PoissonStim:
    def __init__(self, name=None, stim_id=None, interval=None, rev_potential=None, weight=None, tau=None, seed=None, stim_times=None):
        self.name = name
        self.stim_id = stim_id
        self.interval = interval
        self.rev_potential = rev_potential
        self.weight = weight
        self.tau = tau
        self.seed = seed
        self.stim_times = stim_times


class MorphoStimulus:
    def __init__(self, _id, rp, interval, weight, tau, segment, event_times=None):
        self._id = _id
        self.rp = rp
        self.interval = interval
        self.weight = weight
        self.tau = tau
        self.segment = segment
        self.event_times = event_times

    def __repr__(self):
        return f'{self._id} - rp:{self.rp} - interval:{self.interval} - weight:{self.weight} - tau:{self.tau}'

    def connect_to_seg(self, seg):
        # seg: NEURON segment (without the location)
        syn = h.ExpSyn(seg(0.5))
        syn.tau = self.tau
        syn.e = self.rp

        vecstim_times = h.Vector(self.event_times)
        vecstim = h.VecStim()
        vecstim.play(vecstim_times)

        nc = h.NetCon(vecstim, syn)
        nc.weight[0] = self.weight
        nc.delay = 0

        return syn, vecstim, nc


class MorphoStimuli:
    def __init__(self, _id, stim_type_array, segment_array, stim_scaffold, duration):
        # set of excitatory and inhibitory stimuli
        # stim_type_array: list of stim types
        # example ['e', 'e', 'i']
        # segment_array: list of segments the respective stimuli connect to, must be same length as stim_type_array
        # example: [5, 10, 31]
        # stim_params: refers to the StimuliParams object
        self._id = _id
        self.stimuli = [
            MorphoStimulus(
                stim_type,
                stim_scaffold[stim_type].rev_potential,
                stim_scaffold[stim_type].interval,
                stim_scaffold[stim_type].weight,
                stim_scaffold[stim_type].tau,
                segment,
                poisson_process_duration(stim_scaffold[stim_type].interval, duration)
            ) for stim_type, segment in zip(stim_type_array, segment_array)
        ]

        self.syns = []
        self.vecstims = []
        self.ncs = []

    def __repr__(self):
        out = 'Stimuli\n' + '\n'.join([str(stimulus._id) + ' - ' + str(stimulus.segment) for stimulus in self.stimuli])
        return out

    def connect_to_cell(self, connection_points):
        for stimulus in self.stimuli:
            syn, vecstim, nc = stimulus.connect_to_seg(connection_points[stimulus.segment])
            self.syns.append(syn)
            self.vecstims.append(vecstim)
            self.ncs.append(nc)

            
class ExperimentalStimParams:
    # stimuli set used for the point cell experiments
    def __init__(self):
        self.stim_scaffold = {
            'base': {
                'ex': PoissonStim(
                    'ex_base', 'ex_base',
                    interval=5,
                    rev_potential=0,
                    weight=0.0002,
                    tau=2,
                    seed='na'
                ),
                'in': PoissonStim(
                    'in_base', 'in_base',
                    interval=15,
                    rev_potential=-80,
                    weight=0.0005,
                    tau=6,
                    seed='na'
                )
            },
            'lw': {
                'ex': PoissonStim(
                    'ex_lw', 'ex_lw',
                    interval=5,
                    rev_potential=0,
                    weight=0.00015,
                    tau=2,
                    seed='na'
                ),
                'in': PoissonStim(
                    'in_lw', 'in_lw',
                    interval=15,
                    rev_potential=-80,
                    weight=0.0002,
                    tau=6,
                    seed='na'
                )
            },
            'lt': {
                'ex': PoissonStim(
                    'ex_lt', 'ex_lt',
                    interval=5,
                    rev_potential=0,
                    weight=0.0002,
                    tau=10,
                    seed='na'
                ),
                'in': PoissonStim(
                    'in_lt', 'in_lt',
                    interval=15,
                    rev_potential=-80,
                    weight=0.0005,
                    tau=40,
                    seed='na'
                )
            },
            'lwlt': {
                'ex': PoissonStim(
                    'ex_lwlt', 'ex_lwlt',
                    interval=5,
                    rev_potential=0,
                    weight=0.00015,
                    tau=10,
                    seed='na'
                ),
                'in': PoissonStim(
                    'in_lwlt', 'in_lwlt',
                    interval=15,
                    rev_potential=-80,
                    weight=0.0002,
                    tau=40,
                    seed='na'
                )
            },
            'burst': {
                'ex': PoissonStim(
                    'ex_burst', 'ex_burst',
                    interval=5,
                    rev_potential=0,
                    weight=0.0001,
                    tau=40,
                    seed='na'
                ),
                'in': PoissonStim(
                    'in_burst', 'in_burst',
                    interval=15,
                    rev_potential=-80,
                    weight=0.0005,
                    tau=20,
                    seed='na'
                )
            },
            'wb': {
                'ex': PoissonStim(
                    'ex_wb', 'ex_wb',
                    interval=5,
                    rev_potential=0,
                    weight=0.00003,
                    tau=2,
                    seed='na'
                ),
                'in': PoissonStim(
                    'in_wb', 'in_wb',
                    interval=15,
                    rev_potential=-80,
                    weight=0.00005,
                    tau=6,
                    seed='na'
                )
            },
            'pyr': {
                'ex': PoissonStim(
                    'ex_pyr', 'ex_pyr',
                    interval=40,
                    rev_potential=0,
                    weight=0.0015,
                    tau=2,
                    seed='na'
                ),
                'in': PoissonStim(
                    'in_pyr', 'in_pyr',
                    interval=40,
                    rev_potential=-80,
                    weight=0.003,
                    tau=6,
                    seed='na'
                ),
                'stim_type_array': ['ex']*15+['in']*15
            }
        }