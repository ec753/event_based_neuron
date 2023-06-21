#!/bin/bash

# consistent hyperparameters
out_dir='./data/nInputs/'
e_rp=0
i_rp=-80
e_i=5
i_i=15
duration=100000
ospike='ospike' #'ospike' if we want to include the output spike as an event

exp_name='base'
history='base'
e_w=0.0002
e_t=2
i_w=0.0005
i_t=6
for n in {2..30..1}
do
  python ./scripts/nInputs.py ${out_dir} ${exp_name}_${n}_ $n ${duration} ${history} ${ospike} $e_i $e_rp $e_w $e_t $i_i $i_rp $i_w $i_t &
done

exp_name='lw'
history='lw'
e_w=0.00015
e_t=2
i_w=0.0002
i_t=6
for n in {2..30..1}
do
  python ./scripts/nInputs.py ${out_dir} ${exp_name}_${n}_ $n ${duration} ${history} ${ospike} $e_i $e_rp $e_w $e_t $i_i $i_rp $i_w $i_t &
done

exp_name='lt'
history='lt'
e_w=0.0002
e_t=10
i_w=0.0005
i_t=40
for n in {2..30..1}
do
  python ./scripts/nInputs.py ${out_dir} ${exp_name}_${n}_ $n ${duration} ${history} ${ospike} $e_i $e_rp $e_w $e_t $i_i $i_rp $i_w $i_t &
done

exp_name='lwlt'
history='lwlt'
e_w=0.00015
e_t=10
i_w=0.0002
i_t=40
for n in {2..30..1}
do
  python ./scripts/nInputs.py ${out_dir} ${exp_name}_${n}_ $n ${duration} ${history} ${ospike} $e_i $e_rp $e_w $e_t $i_i $i_rp $i_w $i_t &
done

exp_name='burst'
history='burst'
e_w=0.0001
e_t=40
i_w=0.0005
i_t=20
for n in {2..30..1}
do
  python ./scripts/nInputs.py ${out_dir} ${exp_name}_${n}_ $n ${duration} ${history} ${ospike} $e_i $e_rp $e_w $e_t $i_i $i_rp $i_w $i_t &
done

wait


