from game import *
from player import Player
import pickle
import os.path
from os import path


curr_game = Game()

if path.exists("savefile.dat"):
	with open('savefile.dat', 'rb') as f:
		curr_game.poke.hunger, curr_game.poke.happiness, curr_game.poke.level = pickle.load(f)

curr_game.Idle()
while curr_game.running:
    
    if curr_game.snack_flag:
        curr_game.snack_flag = False
        curr_game.eating_running = True
        curr_game.Eat('pink poke puff.png')
 

    elif curr_game.meal_flag:
        
        curr_game.meal_flag = False
        curr_game.eating_running = True
        curr_game.Eat('green poke puff.png')
        

    elif curr_game.play_flag:
        
        curr_game.play_flag = False
        curr_game.idle_running = True
        curr_game.Idle()
        
    elif curr_game.mini_water_flag:
        curr_game.mini_water_flag = False
        curr_game.water_mini_running = True
        curr_game.water_mini()
        
with open('savefile.dat', 'wb') as f:
	pickle.dump([curr_game.poke.hunger, curr_game.poke.happiness, curr_game.poke.level], f, protocol = 2)

