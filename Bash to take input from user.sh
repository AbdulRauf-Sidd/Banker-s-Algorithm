#!bin/bash

read -p "Enter number of process" process

read -p "Enter number of resource types" resource_no

python3 task1.py $process $resource_no
