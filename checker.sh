#!/bin/sh

	ret=$(pstree | grep python3 | wc -l)
	if [ "$ret" -eq 0 ]
then {
	echo "Starting server" #output text
        sleep 1  #delay
	python3 /home/server/Server.py &
	exit 1
}
else 
{
	echo "Ok! Server is run."
	exit 1
}
fi;

