import os 
import subprocess
from sys import platform
import shutil

def build_sar():
    #print("building sar");
    os.chdir("./lib/SourceAutoRecord/")
    if(platform == 'linux'):
        subprocess.Popen('make',shell=True).wait()
        
        portal2d = os.path.join(os.environ["HOME"], ".local/portal2-rl")
        if(not os.path.exists(portal2d)):
            os.mkdir(portal2d)
        shutil.copy2(os.path.join("sar.so"), portal2d)
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
