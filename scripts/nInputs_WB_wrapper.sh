#!/bin/bash

out_dir='../data/nInputs_ospike_WB/'
duration=100000
exp_name='wb'

ew=0.00003
et=2
iw=0.00005
it=6
for n in {2..30..1}
do
  echo ${n}
  python nInputs_WB.py -outdir ${out_dir} -exp_name ${exp_name}_${n}_ -ninputs $n -duration ${duration} -ospike ospike -ei 5 -erp 0 -ew $ew -et $et -ii 15 -irp -80 -iw $iw -it $it&
done

wait