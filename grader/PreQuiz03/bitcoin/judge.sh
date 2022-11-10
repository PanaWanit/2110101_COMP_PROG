#!/bin/bash

for i in {1..5}
do
	pyrun.sh $1 < $i.in > $i.sol
	DIFF=$(diff -w $i.sol $i.out)
	echo -n "Case $i : "
	if [ "$DIFF" != "" ]
	then
		echo "WA"
	else
		echo "PASSED"
	fi
	
done
