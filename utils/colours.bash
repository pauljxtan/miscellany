#!/bin/bash

# A fun reference for Bash colour codes

for i in {40..47}; do
    echo -en " ${i} "
    for j in {30..37}; do
        echo -en "\033[${i};${j}m ${j} "
    echo -en "\033[0m"
    done
    echo
done
