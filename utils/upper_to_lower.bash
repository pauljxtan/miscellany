#!/bin/bash

# Rename all specified files with upper-case replaced by lower-case

for FILE in $*
do
    mv -v "$FILE" `echo $FILE | tr '[A-Z]' '[a-z]'`
done
