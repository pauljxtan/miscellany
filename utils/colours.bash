#!/bin/bash

# A fun reference for Bash colour codes

echo " BG  black   red     green   yellow  blue    magenta cyan    lgray"
for i in {40..47}; do
    echo -en " ${i} "
    for j in {30..37}; do
        echo -en "\033[${i};${j}m ${j}     "
    # turn off colour
    echo -en "\033[0m"
    done
    echo
done

echo

echo " BG   dgray    lred     lgreen   lyellow  lblue    lmagenta lcyan    white"
for i in {100..107}; do
    echo -en " ${i} "
    for j in {90..97}; do
        echo -en "\033[${i};${j}m ${j}      "
    # turn off colour
    echo -en "\033[0m"
    done
    echo
done
