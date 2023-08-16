import os
import numpy as np

from neuron import rxd
from neuron import h

from matplotlib import cm
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly

import sys
sys.path.insert(1, "../../utils/")
import Stimuli, Pyr


data_dir = '../../data/morpho/reconstruct_mccleary/'

def get_simulation_pairs(data_dir):
    files = os.listdir(data_dir)
    seglocIDs = list(set([file.split('_')[2] for file in files]))
    reconstruct_pairs = []
    for file in files:
        if 'origin' in file:
            pairfile = 'reconstruct'+file.strip('origin')
            if pairfile in files:
                reconstruct_pairs.append((file, pairfile))
    return reconstruct_pairs

reconstruct_pairs = get_simulation_pairs(data_dir)
reconstruct_pairs

def calc_sim_pair_mae(origin_file, reconstruct_file, data_dir):
    reconstruct_vs = np.load(f'{data_dir}{reconstruct_file}')
    origin_vs = np.load(f'{data_dir}{origin_file}')
    
    vs_dif = np.abs(origin_vs - reconstruct_vs)
    vs_mae = np.mean(vs_dif, axis=0)
    
    return vs_mae

# load 1
data_dir = '../../data/morpho/reconstruct_mccleary/'
data_dirID = 'mccleary'
reconstruct_pairs = get_simulation_pairs(data_dir)
vs_means = {}

i = 1
for origin_file, reconstruct_file in reconstruct_pairs:
    print(f'{i}/{len(reconstruct_pairs)}')
    i+=1
    seglocID = origin_file.split('_')[2]
    ind = origin_file.split('_')[3].strip('.npy')
    mae = calc_sim_pair_mae(origin_file, reconstruct_file, data_dir)
    vs_means[seglocID+'_'+ind+'_'+data_dirID] = mae

# load 2
data_dir = '../../data/morpho/reconstruct/'
data_dirID = 'home'
reconstruct_pairs = get_simulation_pairs(data_dir)

i = 1
for origin_file, reconstruct_file in reconstruct_pairs:
    print(f'{i}/{len(reconstruct_pairs)}')
    i+=1
    seglocID = origin_file.split('_')[2]
    ind = origin_file.split('_')[3].strip('.npy')
    mae = calc_sim_pair_mae(origin_file, reconstruct_file, data_dir)
    vs_means[seglocID+'_'+ind+'_'+data_dirID] = mae

vs_means_agg = np.array(list(vs_means.values()))
vs_means_agg = np.mean(vs_means_agg, axis=0)

np.save(f'{data_dir}vs_means_agg.npy')