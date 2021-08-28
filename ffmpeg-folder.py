import os
import sys
import subprocess
import pathlib
from pathlib import Path


#current working dir
cwd = os.getcwd()
#parent of cwd
pwd = Path(cwd).parent
#new folder where work will be done
fwd = str(pwd)+'/ffmpeg-folder'

filearray = []

def start(command):
    try: 
        os.mkdir(fwd)
    except OSError as error: 
        print(error)
    count = 1
    for tfile in os.listdir(cwd):
        if os.path.isfile(os.path.join(cwd, tfile)):
            filearray.append(os.path.join(cwd, tfile))
            temp = 'ffmpeg -i "'+ tfile + '" ' + command + ' "' + fwd + "/" + tfile + '"'
            os.system(temp)
        count += 1


def argparse():
    count = 1
    tcommand = ""
    for arg in sys.argv[1:]: 
        tcommand = tcommand + " " + arg
    return tcommand


command = argparse()
start(command)