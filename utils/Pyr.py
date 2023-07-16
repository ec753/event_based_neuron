from neuron import h
from neuron.units import mV, ms
h.load_file("stdrun.hoc")
h.load_file("stdlib.hoc")
h.load_file("import3d.hoc")

import sys
sys.path.insert(1, "../utils/")
from modelDB_87284 import Morse_et_al_2010

class Pyr:
    def __init__(self, recording=False):
        '''
        recording: bool describing whether to record state variables (is expensive)
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

        if recording:
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