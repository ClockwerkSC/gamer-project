from game import *
from player import Player
import pickle
import os.path
from os import path


curr_game = Game()

if path.exists("savefile.dat"):
	with open('savefile.dat', 'rb') as f:
		curr_game.poke.hunger, curr_game.poke.happiness, curr_game.poke.level = pickle.load(f)

while curr_game.running:
    curr_game.Idle()
    if curr_game.snack_flag:
        curr_game.Eat('pink poke puff.png')
    elif curr_game.meal_flag:
        curr_game.Eat('green poke puff.png')
    elif curr_game.play_flag:
        curr_game.Idle()

with open('savefile.dat', 'wb') as f:
	pickle.dump([curr_game.poke.hunger, curr_game.poke.happiness, curr_game.poke.level], f, protocol = 2)

