import numpy as np 
import gym

from gym import Env, spaces
import time

from portal2rl import patch

import os

class Portal2(Env):
    def __init__(self, map="sp_a2_triple_laser", portal2_dir="~/.local/share/Steam/steamapps/common/Portal 2/"): 
        super(Portal2,self).__init__()

        self.location = portal2_dir
        
        if(patch.patch_portal2(portal2_dir) != -1):
            return -1

        pass

