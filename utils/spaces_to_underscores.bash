#!/bin/bash

# Replace spaces in filenames with underscores

for FILE in "$@"
do
    mv -v "$FILE" `echo $FILE | tr ' ' '_'`
done
