
import os
import subprocess
import numpy as np
import shutil
import asyncio
import threading
import struct

from enum import Enum


class DemoInfo:
    header = None
    dem_prot = None
    net_prot = None
    host_name = None
    client_name = None
    map_name = None
    gamedir = None
    time = None
    ticks = None
    frames = None
    tickrate = None
    type_ = None
    sol_length = None # Sign on length

class MessageType(Enum):
    MT_SIGN_ON = 1
    MT_PACKET = 2
    MT_SYNC_TICK = 3
    MT_CONSOLE_CMD = 4
    MT_USER_CMD = 5
    MT_DATA_TABLES = 6
    MT_STOP = 7
    MT_CUSTOM_DATA = 8
    MT_STRING_TABLES = 9

class Message:
    message_type = None
    tick = None
    slot = None # Character
    data = None # message_data_t



demoinf = DemoInfo()

def readStr(x):
    data = x.read(260)
    return data.decode("ascii") 

def readInt(x):
    data = x.read(4)
    return int.from_bytes(data, "little")

def readi8(x):
    data = x.read(1)
    return int.from_bytes(data, "little")

def readFloat(x):
    data = x.read(4)
    return struct.unpack('f', data)

f = open("triple-laser_krzyhau_1230_fixed.dem", mode="rb")

# Set header without the functions, since irregular string length.
data = f.read(8)
demoinf.header = data.decode("ascii")

demoinf.dem_prot = readInt(f)
demoinf.net_prot = readInt(f)
demoinf.host_name = readStr(f)
demoinf.client_name = readStr(f)
demoinf.map_name = readStr(f)
demoinf.gamedir = readStr(f)
demoinf.time = readFloat(f)
demoinf.ticks = readInt(f)
demoinf.frames = readInt(f)
demoinf.sol_length = readInt(f)

print(demoinf.client_name, demoinf.host_name, demoinf.map_name)
print(demoinf.time)
print(demoinf.net_prot, demoinf.dem_prot)
print(demoinf.ticks, demoinf.frames)

for i in range(demoinf.frames+1):
    m = Message()
    m.message_type = readi8(f)
    print(i, m.message_type)
    if(m.message_type == 7):
        break
    m.tick = readInt(f)
    m.slot = readi8(f)

    match m.message_type:
        case 1:
            f.read(76*2)
            f.read(4)
            f.read(4)
            size = readInt(f)
            f.read(size)
        case 2:
            f.read(76*2)
            f.read(4)
            f.read(4)
            size = readInt(f)
            f.read(size)
        case 4:
            size = readInt(f)
            f.read(size)
        case 5:
            print("command")
            cmd = readInt(f)
            size = readInt(f)
            deta = f.read(size)
            print(deta)
        case 6:
            size = readInt(f)
            f.read(size)
        case 8:
            unknown = readInt(f)
            size = readInt(f)
            f.read(size)
        case 9:
            size = readInt(f)
            f.read(size)


# Closing the opened file
f.close()