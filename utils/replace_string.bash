#!/bin/bash

# Replace all occurrences of a string in input files

# Usage: ./replace_string.bash [old] [new] [files...]

SUFFIX=".back"

for FILE in ${@:3}
do
    sed -i$SUFFIX "s/$1/$2/g" $FILE
done
