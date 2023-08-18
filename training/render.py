#!/usr/bin/env python3

import os
import subprocess
import numpy as np


for filename in os.listdir("data/"):
    file = os.path.join("data/", filename)

    if os.path.isfile(file):
        print(file)
        
