import random
import numpy as np

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

class PoissonStimSet:
    # used morphologically detailed neuron models with multiple sources of input stimuli
    def __init__(self, num_stims, all_input_segments, interval, duration, rev_potential, weight, tau):
        stimuli_seg_inds = np.random.choice(np.arange(0, len(all_input_segments)), num_stims, replace=False)
        stimuli_times = [poisson_process_duration(interval, duration) for x in range(num_stims)]
        self.duration = duration
        self.stimuli = [PoissonStim(
            name='ex_' + str(seg_ind),
            stim_id=seg_ind,
            interval=interval,
            rev_potential=rev_potential,
            weight= weight,
            tau = tau,
            seed = np.random.randint(0, 10000000),
            stim_times = stim_times) for seg_ind, stim_times in zip(stimuli_seg_inds, stimuli_times)]

    def write_to_file(self, file_name):
        stimuli_2_file = {
            int(stim.seg_ind):
                {
                    'name': stimuli[seg_ind]._id,
                    'rev_potential': stim.rev_potential,
                    'interval': stim.interval,
                    'weight': stim.weight,
                    'tau': stim.tau,
                    'stim_times': stim.event_times
                } for stim in self.stimuli
        }
        with open(file_name, "w") as fout:
            json.dump(stimuli_2_file, fout)


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
            }
        }