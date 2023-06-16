#!/bin/sh
lstfn="bms.lst"
idev="GPU"
find intel public -name "*.xml" > $lstfn
while read -r line; do
	benchmark_app -d $idev -m $line 
done < $lstfn

