from game import *
from player import Player


idle = Idle()

curr_game = idle


while curr_game.running:
    curr_game.run_game()
    if curr_game.game_flag:
        curr_game = Eat()
    
