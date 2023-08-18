import numpy as np 
import gym

from gym import Env, spaces
import time

import os

class Portal2(Env):
    def __init__(self, map="sp_a2_triple_laser", portal2_dir="~/.local/share/Steam/steamapps/common/Portal 2/"): 
        super(Portal2,self).__init__()

        self.location = portal2_dir


        

