#!/bin/bash
cd ./downloads
for i in *.m4a;
	do ffmpeg -i "$i" -acodec libmp3lame "$(basename "${i/.m4a}")".mp3 && rm "$i"
done
