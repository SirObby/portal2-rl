import os 
import subprocess
from sys import platform

def build_sar():
    #print("building sar");
    os.chdir("./lib/SourceAutoRecord/")
    if(platform == 'linux'):
        subprocess.Popen('make',shell=True).wait()
    elif(platform == 'win32'):
        print("Building for windows is untested.")
        subprocess.Popen('msbuild SourceAutoRecord.sln', shell=True).wait()
    else:
        raise RuntimeError(
            """
            Your current platform environment is not compatible
            with building SourceAutoRecord. 
            portal2-rl only supports the following platforms: linux, win32
            """
        )
