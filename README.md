# portal2-rl

training/render.py script for rendering each individual demo in training/data into training/rendered

portal2-rl.py is the python module for the gym environment.

## How does portal2-rl work?
Source engine games have some very useful things, when you run the game with "-netconport <port>" you can interface with the ingame console through a telnet-like interface. Movement in Source Engine games are handled through console commands, i.e. +jump +forward setang.
