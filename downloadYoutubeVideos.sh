#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Error: please provide input file and path as arguments"
    exit 1
fi

INPUT=$1
PATH=$2

if [ ! -f "$INPUT" ]; then
    echo "Error: input file does not exist"
    exit 1
fi

if [ ! -d "$PATH" ]; then
    echo "Error: path is not a directory"
    exit 1
fi

while IFS= read -r line
do
    sleep 0.25
    #itag 22 equals mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2"
    pytube3 $line --itag='22' -t $PATH
done < "$INPUT
