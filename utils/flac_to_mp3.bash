#!/bin/bash

# Converts FLAC files to mp3, with tags.

for INFILE in "$*"
do
    OUTFILE="${INFILE[@]/%flac/mp3}"

    # TODO: Add more tags if needed
    ALBUM=$(metaflac --show-tag=ALBUM "$INFILE" | sed s/ALBUM=//g)
    ARTIST=$(metaflac --show-tag=ARTIST "$INFILE" | sed s/ARTIST=//g)
    TITLE=$(metaflac --show-tag=TITLE "$INFILE" | sed s/TITLE=//g)
    TRACKNUMBER=$(metaflac --show-tag=TRACKNUMBER "$INFILE" | sed s/TRACKNUMBER=//g)
    TRACKTOTAL=$(metaflac --show-tag=TRACKTOTAL "$INFILE" | sed s/TRACKTOTAL=//g)

    # Encode to mp3 
    # (N.B. need to decode flac separately since it's not supported by lame)
    # TODO: Add more tags if needed

    # (VBR q=0)
    flac -d -c "$INFILE" | lame -V 0 --tl "$ALBUM" --ta "$ARTIST" --tt "$TITLE" --tn "$TRACKNUMBER"/"$TRACKTOTAL" - "$OUTFILE"

    # (CBR 320)
    #flac -d -c "$INFILE" | lame -b 320 --tl "$ALBUM" --ta "$ARTIST" --tt "$TITLE" --tn "$TRACKNUMBER"/"$TRACKTOTAL" - "$OUTFILE"
done
