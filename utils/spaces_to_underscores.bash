#!/bin/bash

# Rename all files in working directory with spaces replaced by underscores
# TODO:
#     Supply filenames as arguments (not sure how to parse args with spaces yet)

for FILE in *
do
    mv -v "$FILE" `echo $FILE | tr ' ' '_'`
done
