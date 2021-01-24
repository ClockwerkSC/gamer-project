import pygame
from player import Player
from menu import *
from hud import Hud
from food import Food
from touch import GameTouch
import os.path

filepath = os.path.dirname(__file__)
background_path = os.path.join(current_path, 'backgrounds') 

class Game():
	def __init__(self):
		pygame.init()

		
		self.DISPLAY_W, self.DISPLAY_H = 800, 480
		self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.Q, self.Z, self.BACK_KEY, self.E, self.ESCAPE = False, False, False, False, False, False, False, False, False  
		self.canvas = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
		self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
		self.running = True
		self.clock = pygame.time.Clock()
		self.main_menu = MainMenu()
		self.eat_menu = EatMenu()
		self.curr_menu = self.main_menu
		self.hud = Hud()
		self.snack_flag = False
		self.meal_flag = False
		self.play_flag = False
		self.mouse_flag = False
		self.mouse_x, self.mouse_y = 0, 0 

		self.poke = Player('croconaw')
		self.touch_display = GameTouch()

	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				
				
				self.running = False
				

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.LEFT_KEY = True
				elif event.key == pygame.K_RIGHT:
					self.RIGHT_KEY = True
				elif event.key == pygame.K_SPACE:
					self.SPACE = True
				elif event.key == pygame.K_BACKSPACE:
					self.BACK_KEY = True 
				elif event.key == pygame.K_q:
					self.Q = True 
				elif event.key == pygame.K_z:
					self.Z = True 
				elif event.key == pygame.K_ESCAPE:
					self.ESCAPE = True
					self.curr_menu.menu_running = True
				elif event.key == pygame.K_e:
					self.E = True
					self.poke.E = True



			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					self.LEFT_KEY = False
				elif event.key == pygame.K_RIGHT:
					self.RIGHT_KEY = False
				elif event.key == pygame.K_SPACE:
					self.SPACE = False
				elif event.key == pygame.K_BACKSPACE:
					self.BACK_KEY = False
				elif event.key == pygame.K_q:
					self.Q = False
				elif event.key == pygame.K_z:
					self.Z = False
				elif event.key == pygame.K_e:
					self.E = False
					self.poke.E = False

			if event.type == pygame.FINGERDOWN:
				
				self.mouse_x, self.mouse_y = event.x, event.y 
				self.mouse_flag = True

	def reset_mouse(self):
		self.mouse_flag = False
			

class Idle(Game):
	def __init__(self):
		Game.__init__(self)
		self.house = pygame.image.load(os.path.join(background_path, 'living room.png'))
	def run_game(self):
		while self.running :
			self.check_events()
			if self.mouse_flag:
				 if self.touch_display.touch_gameloop_checkinput(self.mouse_x, self.mouse_y) == "menu button pressed":
				 	self.ESCAPE = True
				 	self.curr_menu.menu_running = True

				 	


			self.poke.ai_handler()
			self.poke.update()
			self.poke.set_state()
			self.poke.animate() 
			self.canvas.blit(self.house, (0, 0))
			self.poke.draw(self.canvas)
			self.hud.hud_update(self.canvas, self.poke)
			self.touch_display.touch_gameloop_draw(self.canvas)
			self.window.blit(self.canvas, (0,0))
			pygame.display.update()
			self.reset_mouse()


			
			if self.ESCAPE:
				self.canvas.blit(self.house, (0,0))
				self.poke.draw(self.canvas)
				self.hud.hud_update(self.canvas, self.poke)
				self.window.blit(self.canvas, (0,0))
				pygame.display.update()
				self.curr_menu = MainMenu()
				while self.curr_menu.menu_running:
					if self.curr_menu.snack_loop_change == True:
						self.snack_flag = True
						self.curr_menu.menu_running = False
						self.running = False
					elif self.curr_menu.meal_loop_change == True:
						self.meal_flag = True
						self.curr_menu.menu_running = False
						self.running = False
					if self.curr_menu.eat_menu_change:
						self.curr_menu = EatMenu()
						self.curr_menu.eat_menu_change = False
					if self.curr_menu.main_menu_change:
						self.curr_menu = MainMenu()
						self.curr_menu.main_menu_change = False

						

					elif self.curr_menu.play_loop_change:
						self.curr_menu.menu_running = False
						self.curr_menu.play_loop_change = False

					self.curr_menu.check_events()
					self.curr_menu.display_menu(self.canvas)
					self.window.blit(self.canvas, (0,0))
					pygame.display.update()
					self.curr_menu.reset_keys()
					self.curr_menu.mouse_flag = False
					
					

			self.ESCAPE = False
					
class Eat(Game):
	def __init__(self, food):
		Game.__init__(self)
		self.house = pygame.image.load(os.path.join(background_path, 'kitchen.png'))
		self.current_food = Food(food)

	def run_game(self):
		self.poke.kitchen_set_state()
		while self.running:
			self.check_events()
			self.poke.eat()
			self.poke.update()
			
			self.poke.animate()
			self.canvas.blit(self.house, (0,0))
			self.poke.draw(self.canvas)
			self.hud.hud_update(self.canvas, self.poke)
			if self.poke.state == 'eating':
				self.current_food.fooddraw(self.canvas)
			else:
				self.curr_menu = EatMenu()
				while self.curr_menu.menu_running:
					if self.curr_menu.snack_loop_change == True:
						self.snack_flag = True
						self.curr_menu.menu_running = False
						self.running = False
					elif self.curr_menu.meal_loop_change == True:
						self.meal_flag = True
						self.curr_menu.menu_running = False
						self.running = False
					elif self.curr_menu.play_loop_change == True:
						self.play_flag = True
						self.curr_menu.menu_running = False
						self.running = False
					if self.curr_menu.main_menu_change:
						self.curr_menu = MainMenu()
						self.curr_menu.main_menu_change = False
					if self.curr_menu.eat_menu_change:
						self.curr_menu = EatMenu()
						self.curr_menu.main_menu_change = False
					self.curr_menu.check_events()
					self.curr_menu.display_menu(self.canvas)
					self.window.blit(self.canvas, (0,0))
					pygame.display.update()
					self.curr_menu.reset_keys()
					self.curr_menu.mouse_flag = False
				
			self.window.blit(self.canvas, (0,0))
			pygame.display.update()	
			self.poke.reset_keys()

