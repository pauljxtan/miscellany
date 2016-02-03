#!/bin/bash

# Returns the total line count of all files in the current Git repository,
# optionally only for files with a given extension

# Usage: git_line_count [EXTENSION]

if [ -n "$1" ]; then
    git ls-files | grep $1 | xargs cat | wc -l
else
    git ls-files | xargs cat | wc -l 
fi
