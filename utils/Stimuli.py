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


class Poisson_Times:
    # used for the morphologically detailed cell
    def __init__(self, _id, tau, interval, weight, rev_potential, duration=10000, number=99999999,
                 delay=0, start=0):
        '''
        :param _id:
        :param event_times: instead of auto generating, provide a list of event_times
        :param max_time: maximum time (simulation duration)
        :param number: maximum number of stimuli (typically inconsequential if max_time is reasonable)
        '''

        self._id = _id
        self.rev_potential = rev_potential
        self.duration = duration
        self.interval = interval
        self.weight = weight
        self.delay = delay
        self.tau = tau
        self.start = start
        self.number = number
        self.event_times = poisson_process_duration(interval, duration)

    def write2file(self, path):
        stimuli_data = {
            '_id': self._id,
            'rev_potential': self.rev_potential,
            'duration': self.duration,
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


def poisson_times_from_stim_params(stim_params, duration):
    # stim params is the stim_scaffold in MorphoStimParams
    # used for the morphologically detailed cell
    poisson_times = {}
    for _id in stim_params:
        for seg_ind in stim_params[_id]['seg_inds']:
            poisson_times[seg_ind] = Poisson_Times(
                _id,
                stim_params[_id]['tau'],
                stim_params[_id]['interval'],
                stim_params[_id]['weight'],
                stim_params[_id]['rev_potential'],
                duration=duration
            )
    return poisson_times

class MorphoStimParams:
    def __init__(self, pyr):
        self.pyr = pyr
        self.stim_scaffold = {
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
            }
        }