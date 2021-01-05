from game import *

idle = Idle()
curr_game = idle

while curr_game.running:
	curr_game.run_game()