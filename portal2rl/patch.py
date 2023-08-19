import os 
from sys import platform
import sysconfig

# This is the base SAR, I've realized we can't actually use this. 
# Need a version of SAR with the pause and unpause commands.
# Might also have to bind a reset command.
#SAR_SO_DOWNLOAD='https://github.com/p2sr/SourceAutoRecord/releases/download/1.12.7/sar.so'
#SAR_DLL_DOWNLOAD='https://github.com/p2sr/SourceAutoRecord/releases/download/1.12.7/sar.dll'

def log(out:str):
    pass

portal2d = os.path.join(os.environ["HOME"], ".local/portal2-rl")

def patch_portal2(path: str):
    if(os.path.exists(str)):
        if(os.path.exists(os.path.join(path, "sar.so")) or os.path.exists(os.path.join(path, "sar.dll"))):
           log("sar installed, woo") 
        else:
            if(platform == 'linux'):
                #r = requests.get(SAR_SO_DOWNLOAD)  
                #with open(os.path.join(path, 'sar.so'), 'wb') as f:
                #    f.write(r.content)
                log("move sar.so")
                os.move(os.path.join(portal2d,'sar.so'),os.path.join(path,'sar.so'))
            elif(platform == 'win32'):
                #r = requests.get(SAR_DLL_DOWNLOAD)  
                #with open(os.path.join(path, 'sar.dll'), 'wb') as f:
                #    f.write(r.content)
                log("move sar.dll")
            else:
                raise RuntimeError(
                """
                Your current platform environment is not compatible. 
            portal2-rl only supports the following platforms: linux, win32
                """)
    else:
        raise RuntimeError(
        """ 
        The Portal-2 game directory is invalid, this could be, because you entered the wrong path when declaring the Portal2 class.
        """)
    pass
