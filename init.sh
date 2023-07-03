#!/bin/bash

# this initializes a newly downloaded repo to reproduce the results of Cudone et al. 2023

# build data directories
mkdir data
mkdir data/nInputs
mkdir data/nInputs_morpho
mkdir data/nInputs_no_ospike
mkdir data/nInputs_WB
mkdir data/nst_distribution_evolution
mkdir data/nst_distribution_evolution/results
mkdir data/nst_distribution_evolution/stimuli
mkdir data/partial_history
mkdir data/partial_history/results
mkdir data/partial_history_WB
mkdir data/partial_history_WB/results
mkdir data/state_reconstruct
mkdir data/state_reconstruct/original_simulation_data
mkdir data/state_reconstruct/reconstruction_data
mkdir data/state_reconstruct_morpho
mkdir data/state_reconstruct_morpho/original_simulation_data

# build figures directory
mkdir figures

# compile NEURON and move it to where it is needed
nrnivmodl ./mod
cp -r x86_64/ scripts/
cp -r x86_64/ notebooks/
