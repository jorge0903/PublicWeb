#!/usr/bin/env python

from  venv.image import images
import os
import sys


# 0: process.py
# 1: URL
# 2: FILE-TYPE
# 3: APP
# 4: SHARED

        
print('"{}"'.format(sys.argv[0]))
print('"{}"'.format(sys.argv[1]))
print('"{}"'.format(sys.argv[2]))
print('"{}"'.format(sys.argv[3]))
print('"{}"'.format(sys.argv[4]))

if(sys.argv[3] == "Direct" or sys.argv[2] == "Image"):
    print("Downliading with bash from Direct...")
    print(os.system("bash direct.sh" + sys.argv[1]))
    
elif(sys.argv[3] == "Soup" or sys.argv[2] == "Image" or sys.argv[2] == "Picture"):
    try:
        print("Downliading with image script from Soup...")
        images(sys.argv[1])
        
    except:
        print("Downliading with curl from Except Soup...")
        image = "curl -Ok " + sys.argv[1] + " &"
        print(os.system(image))


elif(sys.argv[3] == "Music" or sys.argv[2] == "mp3" or sys.argv[2] == "MP3"):
    try:
        print("Downliading with youtube-dl from Music...")
        song = "cd Music/ && youtube-dl -x --audio-format flac --audio-quality 0 " + sys.argv[1] + " &"
        print(os.system(song))
        
    except:
        print("Downliading with curl from Except Music...")
        image = "ce Music/ && curl -Ok " + sys.argv[1] + " &"
        print(os.system(image))
        

elif(sys.argv[3] == "YouTube"):
    try:
        if(sys.argv[4] == "yes" or sys.argv[4] == "Yes"):
            
            try:
                print("Downliading with youtube-dl  from Video...")
                video = "cd Documentaries/ &&  youtube-dl -f best " + "\"" + sys.argv[1] + "\"" +" &"
                print(os.system(video))

            except:
                print("Downliading with curl from Except Video...")
                image = "cd Documentaries && curl -Ok " + "\"" + sys.argv[1] + "\"" + " &"
                print(os.system(image))
        else:
            try:
                print("Downliading with youtube-dl from Video...")
                print(os.system("cd Not"))
                video = " youtube-dl -f best " + "\"" +sys.argv[1] + "\"" +" &"
                print(os.system(video))

            except:
                print("Downliading with curl from Except Video...")
                print(os.system("cd Not"))
                image = "curl -Ok " + "\"" + sys.argv[1] + "\"" + " &"
                print(os.system(image))
    except:
        try:
            print("Downliading youtuve-dl from Video...")
            video = " youtube-dl -f best " + sys.argv[1] + " &"
            print(os.system(video))

        except:
            print("Downliading curl from Except Video...")
            image = "curl -Ok " + sys.argv[1] + " &"
            print(os.system(image))
                   
        
elif(sys.argv[3] == "Store" or sys.argv[3] == "store" or sys.argv[3] == "Save" or sys.argv[3] == "save"):
    try:
        print("Storing URL...")
        with open("./.URLs", "a") as urls:
            urls.write(sys.argv[1]+"\n")
        
    except Exception as e:
        print("Writing to file from Except...")
        print(str(e))
        storeURL = "echo '" + sys.argv[1] + "' >> .URLs"
        print(os.system(storeURL))
        
else:
    print("Downliading from Other (Last else)...")
    other = "curl -Ok " + "\"" +sys.argv[1] + "\"" + " &"
    print(os.system(other))
    
