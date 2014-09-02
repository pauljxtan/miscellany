#!/bin/bash

# Prints the total RSS memory held by specified user(s), in gigabytes

for USER in $*
do
    echo "$USER:" `ps -u $USER -o rss | awk '{sum+=$1} END {print sum/1024/1024}' && echo "GB"`
done
