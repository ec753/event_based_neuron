import sys
sys.path.insert(1, "../utils/")
import Stimuli, WB

import ctypes
import time
import argparse
import numpy as np
import pandas as pd
from neuron import nrn_dll_sym, h
from neuron.units import ms, mV

h.load_file("stdrun.hoc")
import multiprocessing

#################### ARGUMENTS ###########################
parser = argparse.ArgumentParser(description='Args')
parser.add_argument('-outdir', type=str, help='directory to dump the results to')
parser.add_argument('-exp_name', type=str, help='name of the experiment')
parser.add_argument('-ninputs', type=int, help='number of inputs to include')
parser.add_argument('-duration', type=float, help='duration of each simulation')
parser.add_argument('-ospike', type=str, help='"ospike" if output spike is included')
parser.add_argument('-ei', type=float, help='expected interval of poisson generated excitatory stimuli at each excitatory synapse')
parser.add_argument('-erp', type=float, help='')
parser.add_argument('-ew', type=float, help='')
parser.add_argument('-et', type=float, help='')
parser.add_argument('-ii', type=float, help='')
parser.add_argument('-irp', type=float, help='')
parser.add_argument('-iw', type=float, help='')
parser.add_argument('-it', type=float, help='')
args = parser.parse_args()
##########################################################
# Median and spike histories are generated from simulation in HH_model_specs.ipynb
# currently, they are hard-coded here, not ideal, but should be imported from a file perhaps
# the specific history used is chosen by args.history

median_history = {
    'v': -62.63896424137329, 'm': 0.10259466539537955, 'h': 0.7298860063700434
}
spiking_history = {
    'v': 0.8188187532617182, 'm': 0.313214607214477, 'h': 0.22584291363781567
}

# only difference with hh_n_inputs in nInputs.py is in the spike generation
# we use WB.run_event_sim instead of HH.run_event_sim
def wb_n_inputs(
        last_spike,
        e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23,
        e24, e25, e26, e27, e28, e29, e30, e31, e32, e33, e34, e35, e36, e37, e38, e39,
        i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20, i21, i22, i23,
        i24, i25, i26, i27, i28, i29, i30, i31, i32, i33, i34, i35, i36, i37, i38, i39,
):
    # takes in inputs provided in same manor as pdt event_callback
        # event_times are positive, real-valued times from simulation, relational to the start of the simulation
    # returns the next spike time

    if args.ospike == 'ospike':
        inputs = zip(
            ['o'] + ['e'] * 40 + ['i'] * 40,
            [
                last_spike,
                e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22,
                e23, e24, e25, e26, e27, e28, e29, e30, e31, e32, e33, e34, e35, e36, e37, e38, e39,
                i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20, i21, i22,
                i23, i24, i25, i26, i27, i28, i29, i30, i31, i32, i33, i34, i35, i36, i37, i38, i39
            ]
        )
        inputs = sorted(inputs, key=lambda x: x[1])
    else:
        inputs = zip(
            ['e'] * 40 + ['i'] * 40,
            [
                e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22,
                e23, e24, e25, e26, e27, e28, e29, e30, e31, e32, e33, e34, e35, e36, e37, e38, e39,
                i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20, i21, i22,
                i23, i24, i25, i26, i27, i28, i29, i30, i31, i32, i33, i34, i35, i36, i37, i38, i39
            ]
        )
        inputs = sorted(inputs, key=lambda x: x[1])

    # remove infs
    inputs = [(event_type, event_time) for (event_type, event_time) in inputs if event_time != -np.inf]

    # remove events before last spike
    if args.ospike == 'ospike':
        inputs = [(event_type, event_time) for (event_type, event_time) in inputs if event_time >= last_spike]

    # recenter event times: now they are all non-positive, where the last event received is a time t=0
    # this looks nasty but just recieves the max event_time
    last_event_time = max(enumerate(inputs), key=lambda x: x[1][1])[1][1]
    inputs = [(event_type, event_time - last_event_time) for (event_type, event_time) in inputs]
    # find the starting point of the simulation, it can be 1 of 3 choices:
        # last spike
        # nth latest input
        # first input if # inputs < n
    num_inputs = min(args.ninputs, len(inputs))
    events = inputs[-num_inputs:]

    #print(events)

    if (events[0][0] == 'o') and (args.ospike == 'ospike'):
        # return the spiking history
        history = spiking_history
    elif (events[0][0] == 'e') or (events[0][0] == 'i'):
        history = median_history
    else:
        raise Exception('PROBLEM in the event type')

    # troubleshooting
    #print(len(events), last_spike)
    #print(history)
    '''
    for event in events:
        print(event[0], round(event[1], 3))
    '''
    extra_duration = 20 # refers to the extra simulation duration after the last input event

    spikes = pool.starmap(
        WB.run_event_sim,
        [
            [
                events, history,
                args.ew, args.et, args.erp,
                args.iw, args.it, args.irp,
                extra_duration, False
            ]
        ]
    )[0]
    nsts = [spike for spike in spikes if spike > 0]

    #print(nsts)
    #print()

    if len(nsts) > 0:
        return min(nsts) #+ last_event_time
    else:
        return np.inf


double_ptr = ctypes.POINTER(ctypes.c_double)
on_event_proto = ctypes.CFUNCTYPE(*([ctypes.c_double] * 82)) # 1 for return, 1 for last spike, 40 for each stim type

on_event_c = on_event_proto(wb_n_inputs)
on_event_c_ptr = ctypes.cast(on_event_c, double_ptr)

nrn_hocobj_ptr = nrn_dll_sym("nrn_hocobj_ptr")
nrn_hocobj_ptr.restype = ctypes.py_object
event_callback_ptr = nrn_hocobj_ptr(ctypes.cast(on_event_c_ptr, double_ptr))

if __name__ == '__main__':
    '''
    print(f'outdir:{args.outdir}')
    print(f'exp_name:{args.exp_name}')
    print(f'ninputs:{args.ninputs}')
    print(f'duration:{args.duration}')
    print(f'ospike:{args.ospike}')
    print(f'ex_i:{args.ei}')
    print(f'ex_w:{args.ew}')
    print(f'ex_t:{args.et}')
    print(f'ex_rp:{args.erp}')
    print(f'in_i:{args.ii}')
    print(f'in_w:{args.iw}')
    print(f'in_t:{args.it}')
    print(f'in_rp:{args.irp}')
    '''


    pool = multiprocessing.Pool(1)

    # set up cellNST
    #print('initializing cellNST in NEURON')
    cellNST = h.nInputs40()
    cellNST._ref_on_event = event_callback_ptr
    cellNST_spikes = h.Vector()
    cellNST_nc = h.NetCon(cellNST, None)
    cellNST_nc.record(cellNST_spikes)


    # excitatory stimuli
    estim = h.NetStim()
    estim.noise = True
    estim.interval = args.ei * ms
    estim.number = 10_000_000 # arbitrary
    estim.start = 0 * ms
    estim.seed(11)
    # connect to cellNST
    e_nc_nst = h.NetCon(estim, cellNST)
    e_nc_nst.delay = 0
    e_nc_nst.weight[0] = args.ew

    e_stims = h.Vector()
    e_nc_nst.record(e_stims)

    # inhibitory stimulus
    istim = h.NetStim()
    istim.noise = True
    istim.interval = args.ii * ms
    istim.number = 10_000_000
    istim.start = 0 * ms
    istim.seed(42)
    # connect to cellNST
    i_nc_nst = h.NetCon(istim, cellNST)
    i_nc_nst.delay = 0
    i_nc_nst.weight[0] = -args.iw
    # i_nc_nst.weight is negative because the h.nInputs40 cell distinguishes excitatory from inhibitory
    # stimuli by the sign of their weight (the magnitude of the weight is arbitrary)

    i_stims = h.Vector()
    i_nc_nst.record(i_stims)

    #################################################
    # Run simulation
    #################################################
    #print('running simulation')
    h.finitialize(-65 * mV)

    start = time.perf_counter()
    h.continuerun(args.duration * ms)
    stop = time.perf_counter()
    #print(f"simulation took {stop - start} seconds")
    #print(list(e_stims))
    #print(list(i_stims))

    pool.close()

    # write results to file
    with open(f'{args.outdir}/{args.exp_name}_{args.ninputs}_estims.txt', 'w') as f:
        for item in e_stims:
            f.write("%s\n" % item)
    with open(f'{args.outdir}/{args.exp_name}_{args.ninputs}_istims.txt', 'w') as f:
        for item in i_stims:
            f.write("%s\n" % item)
    with open(f'{args.outdir}/{args.exp_name}_{args.ninputs}_spikes.txt', 'w') as f:
        for item in cellNST_spikes:
            f.write("%s\n" % item)