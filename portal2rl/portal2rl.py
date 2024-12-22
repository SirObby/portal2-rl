from typing import Optional
import numpy as np 

import time
import gymnasium as gym

import asyncio

#import os

class Portal2(gym.Env):
    def __init__(self, map: str="sp_a2_triple_laser", portal2_dir: str ="~/.local/share/Steam/steamapps/common/Portal 2/"): 
        super(Portal2,self).__init__()

        self.location = portal2_dir
        
        self._view_angles_y = 0;
        self._view_angles_x = 0;

        #self._run_game()

        #self.action_space = gym.spaces.Discrete(4)

        pass
    async def _run_game(self):
        proc = await asyncio.subprocess.create_subprocess_exec("~/.steam/steam/ubuntu12_32/steam-runtime/run.sh", f"{PORTAL2_DIRECTORY}/portal2.sh", "-game", "portal2", "-steam", "-novid", "-windowed","-vulkan", "-w", "960", "-h", "540", "-netconport", "2999", "0", cwd=PORTAL2_DIRECTORY)
        # ~/.steam/steam/ubuntu12_32/steam-runtime/run.sh "~/.local/share/Steam/steamapps/common/Portal 2/portal2.sh" -game portal2 -steam -novid -windowed -vulkan -w 960 -h 540 -netconport 2999

        pass
    def _get_obs(self):
        return {}
    def _get_info(self):
        return {}
    def reset(self, map: Optional[str]="sp_a2_triple_laser", portal2_dir: Optional[str] ="~/.local/share/Steam/steamapps/common/Portal 2/"):
        # We need the following line to seed self.np_random
        super().reset()

        # Choose the agent's location uniformly at random
        #self._agent_location = self.np_random.integers(0, self.size, size=2, dtype=int)

        # We will sample the target's location randomly until it does not coincide with the agent's location
        #self._target_location = self._agent_location
        #while np.array_equal(self._target_location, self._agent_location):
        #    self._target_location = self.np_random.integers(
        #        0, self.size, size=2, dtype=int
        #    )

        observation = self._get_obs()
        info = self._get_info()

        return observation, info
    def step(self, action):
        # Map the action (element of {0,1,2,3}) to the direction we walk in
        #direction# = self._action_to_direction[action]
        # We use `np.clip` to make sure we don't leave the grid bounds
        #self._agent_location = np.clip(
        #    self._agent_location + direction, 0, self.size - 1
        #)

        # An environment is completed if and only if the agent has reached the target
        #terminated = np.array_equal(self._agent_location, self._target_location)
        truncated = False
        reward = 1 #if terminated else 0  # the agent is only reached at the end of the episode
        observation = self._get_obs()
        info = self._get_info()

        return observation, reward, terminated, truncated, info
    
gym.register(
    id="portal2-rl/Portal2",
    entry_point=Portal2,
)