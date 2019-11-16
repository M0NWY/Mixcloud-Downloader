# Script of getting mixes off of Mixcloud
import os.path
import time
import subprocess
import requests
import re
from subprocess import call
import shutil
import sys	

# genres are literal url paths after /discover you can add or remove them to your liking
# dump file full of links only.

for genre in ["beats", "deep-house", "drum-bass", "dubstep", "edm", "electronica", "house", "tech-house", "techno", "trance", "science"] :
   command = "lynx -dump -listonly www.mixcloud.com/discover/"
   command += genre
   command += " > urls.txt"
   call(command, shell=True)
   printy = "dumped urls for : "
   printy += genre
   print(printy)

# for every line in file see if is a good url and strip out ones we don't want

   with open("urls.txt") as file:
      for line in file :
         
         url = re.findall(r'(https?://www.mixc[^\s]+)', line)
         url = str(url)
         if url :
            slashes = url.count("/") # ensure correct path depth
            select = url.count("select") # thise are just links to more lists
            discover = url.count("discover")

            if slashes == 5 and select == 0 and discover == 0 :
               # string cleaning
               url = url.replace("[","")
               url = url.replace("]","")
               url = url[1:]
               url = url[:-1]
               print("URL:"),
               print(url)

               # Grab raw website and pull out link to segments using the waveform url!

               sess = requests.Session()
               r = sess.get(url)
               segpath = re.search(r'(https://waveform.mixcloud.com/)(.+)(.json)', r.text)
               if not segpath :
                  print("Could not extract valid path, NEXT !!")
                  continue
               print("Path :"),
               print( segpath.group(2) )

               # for each mix we need to go and get all segments
               # filename generation
               
               filename = url[25:]
               filename = filename[:-1]
               filename = filename.replace("/","-")
               noext = filename

               filename += ".m4a"
               
               print("Filename : "),
               print(filename),
               print(" , Length : "),
               print(len(filename))
               if len(filename) > 250 :
                  filename = filename[:250]
			  # have we already got this one ?
               filepath = "./downloads/"
               checkfilenameandpath = filepath + filename
               if os.path.exists(checkfilenameandpath) :
                  print("Allready got this one, NEXT!!")
                  continue
				  
				  
              # there is an initial segment !
               wginitcom = "wget -nc -q -O ./downloads/segs/frag0 "
               wginitcom += "https://audio8.mixcloud.com/secure/dash2/"
               wginitcom += segpath.group(2)
               wginitcom += ".m4a/init-a1-x3.mp4"
               
               wgetreturned = call(wginitcom, shell=True)
               segcount = 1
               if wgetreturned != 0 :
                  call("rm ./downloads/segs/*", shell=True)
                  print("Can't get initial segemnt, NEXT !!")
                  continue
				  
               while wgetreturned == 0:
                  segurl = "https://audio8.mixcloud.com/secure/dash2/"
                  segurl += segpath.group(2)
                  segurl += ".m4a/fragment-"

                  segurl += str(segcount)
                  segurl += "-a1-x3.m4s"
                  # build wget command 
                  segcom = "wget -nc -q -O ./downloads/segs/frag"
                  segcom += str(segcount)
                  segcom += " "
                  segcom += segurl
                  #execute command
                  wgetreturned = call(segcom, shell=True)
                  
                  sys.stdout.write("Downloading segment: %d   \r" % (segcount) )
                  sys.stdout.flush()
                  segcount += 1               
                              
               # mmmmmmm.... sticky sticky gluey gluey...
               print("     Done          ")
               print("Glueing it all together")
               outfilename = "./downloads/" + filename
               with open(outfilename, 'wb') as outfile:
                  for number in range(segcount):
                     stickyfilename = "./downloads/segs/frag"
                     stickyfilename += str(number)
                     
                     with open(stickyfilename, 'rb') as readfile:
                        shutil.copyfileobj(readfile, outfile)               
               
               call("rm ./downloads/segs/*", shell=True) 
               
           
print(" Woooot.. converting to mp3 ")
call("./convert.sh", shell=True)

print("Phew... done")
