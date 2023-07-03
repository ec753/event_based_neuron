#!/bin/bash

#SBATCH --job-name=reconstruct
#SBATCH --output ../slurm_out/reconstruct.txt
#SBATCH --time 10:00:00
#SBATCH --ntasks 6
#SBATCH --mail-type=ALL
#SBATCH --mem 20G

module load miniconda
source ../venv/bin/activate

python state_reconstruct_part1.py

python state_reconstruct_part2.py 'base' &
python state_reconstruct_part2.py 'lw' &
python state_reconstruct_part2.py 'lt' &
python state_reconstruct_part2.py 'lwlt' &
python state_reconstruct_part2.py 'burst' &
python state_reconstruct_part2.py 'wb' &

wait



