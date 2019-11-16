# Mixcloud-Downloader
A python script for downloading the latest mixcloud mixes

The main script is calld jointer2 as it goes and gets the many fragments nessasary to rebuild the original m4a file.

Written in order to get a load of mixes to stick on a stick to stick in my van.

This is the latest and greatest version of my tool current as of 16/11/2019
Requires a /download and /download/seg folders to be present from whereever you are running it.

It will complain violently / die if there are files in the /seg dir.

Requires ffmpeg, wget, and lynx ! ( I know, I know, I'll write lynx out of it later )

Also needs python module: requests which I can't remember if it's standard.
