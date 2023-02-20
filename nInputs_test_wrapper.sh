#!/bin/bash

# consistent hyperparameters
out_dir='./data/test_nInputs/'
e_rp=0
i_rp=-80
e_i=5
i_i=15
duration=1000
ospike='noospike'

exp_name='test_no_ospike'
history='base'
e_w=0.0002
e_t=2
i_w=0.0005
i_t=6
for n in {10..10..1}
do
  python ./scripts/nInputs.py ${out_dir} ${exp_name}_${n}_ ${n} ${duration} ${history} ${ospike} $e_i $e_rp $e_w $e_t $i_i $i_rp $i_w $i_t &
done

wait


