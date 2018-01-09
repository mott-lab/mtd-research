#!/bin/bash

# script to make persistent dirs inside ../proj/hostfiles
dirCount=0
for((i=1;i<11;i++)); do
	# check if directories exist; create them if not there
	if [ -d "/home/mininet/mininet/proj/hostfiles/h${i}" ]; then
		echo "h${i}/ directory already exists. Skipping."
	else
		mkdir /home/mininet/mininet/proj/hostfiles/h${i}
		let dirCount="dirCount += 1"
	fi

	if [ -d "/home/mininet/mininet/proj/hostfiles/h${i}/var" ]; then
                echo "h${i}/var directory already exists. Skipping."
        else
                mkdir /home/mininet/mininet/proj/hostfiles/h${i}/var
		let dirCount="dirCount += 1"
        fi

	if [ -d "/home/mininet/mininet/proj/hostfiles/h${i}/var/run" ]; then
                echo "h${i}/var/run directory already exists. Skipping."
        else
                mkdir /home/mininet/mininet/proj/hostfiles/h${i}/var/run
		let dirCount="dirCount += 1"
        fi

	if [ -d "/home/mininet/mininet/proj/hostfiles/h${i}/var/log" ]; then
                echo "h${i}/var/log directory already exists. Skipping."
        else
                mkdir /home/mininet/mininet/proj/hostfiles/h${i}/var/log
		let dirCount="dirCount += 1"
        fi

	# line below simply runs `mkdir` on all dirs.
	# echo `mkdir h${i} h${i}/var h${i}/var/run h${i}/var/log`

	# cp timer.sh to host root dir. Do not check if already exists so that user can overwrite each host's files easily if he/she makes changes to timer.sh.
	cp /home/mininet/mininet/proj/hostfiles/timer.sh /home/mininet/mininet/proj/hostfiles/h${i}/
	echo "timer.sh copied into h${i}/"
done
echo "$dirCount missing directories created."
