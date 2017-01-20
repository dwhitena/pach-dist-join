#!/bin/bash

FILES=*

pachctl create-repo patient_measurements
commitid=$(pachctl start-commit patient_measurements master) 

for f in $FILES
do
	if [ $f != "load.sh" ]
	then
		echo $f
		pachctl put-file patient_measurements $commitid $f -f $f
	fi
done

pachctl finish-commit patient_measurements $commitid
