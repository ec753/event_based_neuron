#!/bin/bash

# This wrapper wraps the nInputs_morpho.py script in ./scripts/


out_dir='./data/test_nInputs_morpho/'
exp_name='test'
duration=10000

e_n=10
e_i=5
e_rp=0
e_w=0.2
e_t=2

i_n=5
i_i=10
i_rp=-80
i_w=0.5
i_t=6

for n in {21..40..1}
do
  echo $exp_name $n
  python ./scripts/nInputs_morpho.py \
    -outdir ${out_dir} \
    -exp_name ${exp_name}_${n}_ \
    -ninputs $n \
    -duration ${duration} \
    -num_excitatory_stims $e_n \
    -excitatory_interval $e_i \
    -excitatory_rev_potential $e_rp \
    -excitatory_weight $e_w \
    -excitatory_tau $e_t \
    -num_inhibitory_stims $e_n \
    -inhibitory_interval $e_i \
    -inhibitory_rev_potential $e_rp \
    -inhibitory_weight $e_w \
    -inhibitory_tau $e_t &
done