#!/bin/bash

for i in {1..8}
do
	pyrun.sh $1 < $i.in > $i.out
	DIFF=$(diff -w $i.sol $i.out)
	echo -n "Case $i : "
	if [ "$DIFF" != "" ]
	then
		echo "WA"
	else
		echo "PASSED"
	fi
	
done
