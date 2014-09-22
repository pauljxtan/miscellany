#!/bin/bash

# Get the CPU model

MODELNAME=`cat /proc/cpuinfo | grep "model name" | sed -e "s/.*: //" | uniq`
CPUCORES=`cat /proc/cpuinfo | grep "cpu cores" | sed -e "s/.*: //" | uniq`
echo "${MODELNAME} ($CPUCORES cores)"
