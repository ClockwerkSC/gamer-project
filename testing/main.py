from game import *
from player import Player


idle = Idle()

curr_game = idle


while curr_game.running:
    curr_game.run_game()
    if curr_game.snack_flag:
        curr_game = Eat('pink poke puff.png')
    elif curr_game.meal_flag:
        curr_game = Eat('green poke puff.png')
    elif curr_game.play_flag:
        curr_game = Idle()

