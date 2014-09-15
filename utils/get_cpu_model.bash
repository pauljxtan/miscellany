#!/bin/bash

# Get the CPU model

cat /proc/cpuinfo | grep "model name" | sed -e "s/.*: //" | uniq
