import pygame
from player import Player
from menu import *
from hud import Hud
from food import Food

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
		self.idle_running = True
		self.eating_running = True

		self.poke = Player('croconaw')

	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				
				
				self.running = False
				self.idle_running = False
				self.eating_running = False
				

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

	def Idle(self):
		self.house = pygame.image.load('backgrounds/living room.png')
		self.poke.rect.midbottom = (240, 450)
		while self.idle_running:
			self.check_events()
			self.poke.ai_handler()
			self.poke.update()
			self.poke.set_state()
			self.poke.animate() 
			self.canvas.blit(self.house, (0, 0))
			self.poke.draw(self.canvas)
			self.hud.hud_update(self.canvas, self.poke)
			self.window.blit(self.canvas, (0,0))
			pygame.display.update()


			if self.ESCAPE:
				while self.curr_menu.menu_running:
					if self.curr_menu.snack_loop_change == True:
						self.snack_flag = True
						self.curr_menu.menu_running = False
						self.idle_running = False
					elif self.curr_menu.meal_loop_change == True:
						self.meal_flag = True
						self.curr_menu.menu_running = False
						self.idle_running = False
					if self.curr_menu.eat_menu_change:
						self.curr_menu = EatMenu()
						self.curr_menu.eat_menu_change = False
					elif self.curr_menu.play_loop_change:
						self.curr_menu.menu_running = False
						self.curr_menu.play_loop_change = False

					self.curr_menu.check_events()
					self.curr_menu.display_menu(self.canvas)
					self.window.blit(self.canvas, (0,0))
					pygame.display.update()
					self.curr_menu.reset_keys()

					
	def Eat(self, food):
		self.house = pygame.image.load('backgrounds/kitchen.png')
		self.current_food = Food(food)
		self.poke.kitchen_set_state()
		self.poke.current_frame = 0
		while self.eating_running:
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
						self.eating_running = False
					elif self.curr_menu.meal_loop_change == True:
						self.meal_flag = True
						self.curr_menu.menu_running = False
						self.eating_running = False
					elif self.curr_menu.play_loop_change == True:
						self.play_flag = True
						self.curr_menu.menu_running = False
						self.eating_running = False
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
				
			self.window.blit(self.canvas, (0,0))
			pygame.display.update()	
			self.poke.reset_keys()

