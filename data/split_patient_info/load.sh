#!/bin/bash

FILES=*

pachctl create-repo patient_info
commitid=$(pachctl start-commit patient_info master) 

for f in $FILES
do
	if [ $f != "load.sh" ]
	then
		echo $f
		pachctl put-file patient_info $commitid $f -f $f
	fi
done

pachctl finish-commit patient_info $commitid
