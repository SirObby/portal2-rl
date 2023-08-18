import os 
from sys import platform

# This is the base SAR, I've realized we can't actually use this. 
# Need a version of SAR with the pause and unpause commands.
# Might also have to bind a reset command.
SAR_SO_DOWNLOAD='https://github.com/p2sr/SourceAutoRecord/releases/download/1.12.7/sar.so'
SAR_DLL_DOWNLOAD='https://github.com/p2sr/SourceAutoRecord/releases/download/1.12.7/sar.dll'

def log(out:str):
    pass

def patch_portal2(path: str):
    if(os.isdir(str)):
        if(os.path.exists(os.path.join(path, "sar.so")) or os.path.exists(os.path.join(path, "sar.dll"))):
           log("sar installed, woo") 
        else:
            if(platform == 'linux'):
                r = requests.get(SAR_SO_DOWNLOAD)  
                with open(os.path.join(path, 'sar.so'), 'wb') as f:
                    f.write(r.content)
                log("download sar.so")
            elif(platform == 'win32'):
                r = requests.get(SAR_DLL_DOWNLOAD)  
                with open(os.path.join(path, 'sar.dll'), 'wb') as f:
                    f.write(r.content)
                log("download sar.dll")
            else:
                print("???????? what are you using??????")
    else:
        print("Portal 2 not found at directory, could be that you don't have it in the Steam default path, or that you defined the wrong one in the Portal2 class.")
        return -1
    pass
