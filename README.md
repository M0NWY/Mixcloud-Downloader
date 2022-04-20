# Mixcloud-Downloader

Now no-longer works - I'll be making a better one later with full selenium and youtube-dl
You can probably get what you want done with just YouTube-dl - now live : https://github.com/M0NWY/Mixcloud-Downloader-2

A python script for downloading the latest mixcloud mixes

Setup : 

mkdir downloads
        
mkdir downloads/segs

Usage : python3 jointer2.py

The main script is calld jointer2 as it goes and gets the many fragments nessasary to rebuild the original m4a file.

Written in order to get a load of mixes to stick on a stick to stick in my van.

This is the latest and greatest version of my tool current as of 16/11/2019
Requires a /download and /download/seg folders to be present from whereever you are running it.

It will complain violently / die if there are files in the /seg dir.

Requires ffmpeg, wget, and lynx ! ( I know, I know, I'll write lynx out of it later )

Also needs python module: requests which I can't remember if it's standard.

Oh and it's best to run it a couple of days before you want the tunes. It is slow. 
