#!/bin/bash

# This wrapper wraps the nInputs_morpho.py script in ./scripts/


out_dir='./data/nInputs_morpho/'
exp_name='test'
duration=10000

python ./scripts/nInputs_morpho.py -outdir ${out_dir} -exp_name ${exp_name}_${n}_ &