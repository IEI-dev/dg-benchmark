#!/bin/sh
lstfn="bms.lst"
idev="GPU.1"
find intel public -name "*.xml" > $lstfn
while read -r line; do
	echo "benchmarking GPU with $line"
	benchmark_app -d $idev -m $line 
done < $lstfn

