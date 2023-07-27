#!/bin/bash

#SBATCH --job-name=stim_locs2
#SBATCH --output slurm_out.stim_locs02.txt
#SBATCH --time 1-
#SBATCH --ntasks 10
#SBATCH --mail-type=ALL
#SBATCH --mem 20G

module load miniconda
source ../../venv/bin/activate

python initialize_stimuli_locs.py &
python initialize_stimuli_locs.py &
python initialize_stimuli_locs.py &
python initialize_stimuli_locs.py &
python initialize_stimuli_locs.py &
python initialize_stimuli_locs.py &
python initialize_stimuli_locs.py &
python initialize_stimuli_locs.py &
python initialize_stimuli_locs.py &
python initialize_stimuli_locs.py &
python initialize_stimuli_locs.py &

wait
