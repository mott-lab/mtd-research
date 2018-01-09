#!/bin/bash

# simple timer script that prints out the date every 3 seconds

while true; do
	echo "PID: $$"
	printf "Current date and time: %s\n" "$(date)"
	sleep 3
done
