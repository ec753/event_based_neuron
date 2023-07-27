from neuron import h
from neuron.units import mV, ms
h.load_file("stdrun.hoc")
h.load_file("stdlib.hoc")
h.load_file("import3d.hoc")

import json

import sys
sys.path.insert(1, "../utils/")
from modelDB_87284 import Morse_et_al_2010

class Pyr:
    def __init__(self, vm_recording=False):
        '''
        _id: currently used to denote the specific input seg pattern
            matters when spike_history_recording == True
        vm_recording: bool describing whether to record membrane voltage (is expensive)
        spike_history_recording: bool describing whether to record state variables on output spikes, writes to outdir
        '''

        self.cell = Morse_et_al_2010()
        self.connection_points = self.cell.apic + self.cell.basal  # where stimuli can be connected
        self.all_segs = [self.cell.soma, self.cell.axon] + self.cell.basal + self.cell.apic
        self.all_seg_locs = [str(seg).split('.')[1].split('[')[0] for seg in self.all_segs]

        # increase passive leak to inhibit tonic spiking
        for sec in self.cell.axon.wholetree():
            for seg in sec:
                seg.pas.g *= 2.5

        # setup recording
        self.spike_times = h.Vector()
        self.nc_self = h.NetCon(self.cell.axon(0.5)._ref_v, None, sec=self.cell.axon)
        self.nc_self.threshold = 0
        self.nc_self.record(self.spike_times)

        if vm_recording:
            self._t = h.Vector().record(h._ref_t)
            self._vs = [h.Vector().record(seg._ref_v) for sec in self.all_segs for seg in sec]

    def add_stimuli(self, morpho_stimuli):
        '''
        morpho_stimuli: of the MorphoStimuli class
        '''
        self.stimuli = morpho_stimuli
        self.stimuli.connect_to_cell(self.connection_points)

    def run_simulation(self, duration):
        h.celsius = 35
        h.finitialize(-65)
        h.continuerun(duration * ms)

    def all_state_vars(self):
        all_state_vars = {}
        for seg in self.all_segs:
            all_state_vars[str(seg)] = get_state_vars(seg)
        return all_state_vars

    def initialize_state_vars(self, history_file):
        # initializes all state variables using a history_file (json)
        # this history file is the json output of get_state_vars() for all secs
        with open(history_file) as fin:
            history = json.load(fin)
        for seg in self.all_segs:
            seg_history = history[str(seg)]
            secs = [sec for sec in seg]
            history_walk(seg_history, secs)

def history_walk(seg_history, secs):
    # walks the pyr morphology and the history json simultaneously using recursion
    for key, item in seg_history.items():
        if type(item) is dict:
            if len(item.keys()) > 0:
                new_seg_history = item
                new_secs = [getattr(sec, str(key)) for sec in secs]
                history_walk(new_seg_history, new_secs)
        else:
            for val, sec in zip(item, secs):
                setattr(sec, key, val)

def get_state_vars(sec):
    # retrieves the state vars of the given section

    results = {}
    mname = h.ref("")
    center_seg_dir = dir(sec(0.5))
    mechs_present = []

    # membrane mechanisms
    mt = h.MechanismType(0)

    for i in range(int(mt.count())):
        mt.select(i)
        mt.selected(mname)
        name = mname[0]
        if name in center_seg_dir:
            mechs_present.append(name)

    for mech in mechs_present:
        my_results = {}
        ms = h.MechanismStandard(mech, 3)
        for j in range(int(ms.count())):
            n = int(ms.name(mname, j))
            name = mname[0]
            pvals = []
            # TODO: technically this is assuming everything that ends with _ion
            #       is an ion. Check this.
            if mech.endswith("_ion"):
                pvals = [getattr(seg, name) for seg in sec]
            else:
                mechname = name  # + '_' + mech
                for seg in sec:
                    if n > 1:
                        pvals.append([getattr(seg, mechname)[i] for i in range(n)])
                    else:
                        pvals.append(getattr(seg, mechname))
            my_results[
                name[: -(len(mech) + 1)] if name.endswith("_" + mech) else name
            ] = pvals
        # TODO: should be a better way of testing if an ion
        if not mech.endswith("_ion"):
            results[mech] = my_results

    results["v"] = [seg.v for seg in sec]

    return results

