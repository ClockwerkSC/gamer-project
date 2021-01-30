import pygame
from player import Player
from menu import *
from hud import DefaultHud, WaterHud
from food import Food
from touch import PartialTouch, FullTouch
from minigames.watergame.watercharacter import WaterCharacter
from minigames.watergame.magicarp import Magicarp
import random
import math
class Game():
	def __init__(self):
		pygame.init()
		self.DISPLAY_W, self.DISPLAY_H = 800, 480
		self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.SPACE, self.Q, self.Z, self.BACK_KEY, self.E, self.ESCAPE = False, False, False, False, False, False, False, False, False, False, False, False 
		self.canvas = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
		self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
		self.running = True
		self.clock = pygame.time.Clock()
		self.main_menu = MainMenu()
		self.eat_menu = EatMenu()
		self.curr_menu = self.main_menu
		self.hud = DefaultHud()
		self.snack_flag = False
		self.meal_flag = False
		self.play_flag = False
		self.mini_water_flag = False
		self.idle_running = True
		self.eating_running = True
		self.water_mini_running = True
		self.clock = pygame.time.Clock()
		self.water_high_score = 0
		self.poke = Player('croconaw')
		self.fingers = {}

	def check_events(self, touchcontrol = False):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
				self.idle_running = False
				self.eating_running = False
				self.water_mini_running = False

			if touchcontrol != False:
				if event.type == pygame.FINGERDOWN:
					self.fingers[event.finger_id] = {'x': event.x * self.DISPLAY_W, 'y': event.y * self.DISPLAY_H, 'fresh_pressed': True}
				
				elif event.type == pygame.FINGERMOTION:
					if event.finger_id in self.fingers:
						self.fingers[event.finger_id].update({'x': event.x * self.DISPLAY_W, 'y': event.y * self.DISPLAY_H, 'fresh_pressed': False})

				elif event.type == pygame.FINGERUP:
					if event.finger_id in self.fingers:
						del self.fingers[event.finger_id]

				keys = pygame.key.get_pressed()
				if self.fingers == {} and (keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False and keys[pygame.K_UP] == False and keys[pygame.K_DOWN] == False):
					self.LEFT_KEY, self.RIGHT_KEY, self.UP_KEY, self.DOWN_KEY = False, False, False, False
				else:
					for finger in list(self.fingers):
						touchcontrol.touch_input(self.fingers.get(finger))
						if touchcontrol.MENU_BUTTON:
							self.ESCAPE = True
							del self.fingers[finger]
						if touchcontrol.A:
							self.START_KEY = True
							self.SPACE = True
							del self.fingers[finger]
						if touchcontrol.B:
							self.BACK_KEY = True
							del self.fingers[finger]
						if touchcontrol.LEFT:
							self.LEFT_KEY = True
						elif touchcontrol.RIGHT:
							self.RIGHT_KEY = True
						
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

			elif event.type == pygame.KEYUP:
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

	def reset_fingers(self):
		self.fingers = {}

	def reset_keys(self):
		self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.SPACE, self.Q, self.Z, self.BACK_KEY, self.E, self.ESCAPE = False, False, False, False, False, False, False, False, False, False, False, False 		

	def Idle(self):
		self.house = pygame.image.load('../assets/backgrounds/living room.png')
		self.poke.rect.midbottom = (240, 450)
		self.touch_idle = PartialTouch()
		while self.idle_running:
			self.check_events(self.touch_idle)
			self.poke.ai_handler()
			self.poke.update()
			self.poke.set_state()
			self.poke.animate() 
			self.canvas.blit(self.house, (0, 0))
			self.poke.draw(self.canvas)
			self.hud.hud_update(self.canvas, self.poke)
			self.touch_idle.touch_draw(self.canvas)
			self.window.blit(self.canvas, (0,0))
			pygame.display.update()
			
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
						self.idle_running = False
					elif self.curr_menu.meal_loop_change == True:
						self.meal_flag = True
						self.curr_menu.menu_running = False
						self.idle_running = False
					if self.curr_menu.eat_menu_change:
						self.curr_menu = EatMenu()
						self.curr_menu.eat_menu_change = False
					if self.curr_menu.main_menu_change:
						self.curr_menu = MainMenu()
						self.curr_menu.main_menu_change = False
					if  self.curr_menu.mini_menu_change:
						self.curr_menu = MiniMenu()
						self.curr_menu.mini_menu_change = False
					elif self.curr_menu.play_loop_change:
						self.curr_menu.menu_running = False
						self.curr_menu.play_loop_change = False
					if self.curr_menu.mini_water_loop_change:
						self.curr_menu.menu_running = False
						self.mini_water_flag = True
						self.curr_menu.mini_water_loop_change = False
						self.idle_running = False
					
					self.curr_menu.check_events(self.curr_menu.menu_touch)	
					self.curr_menu.display_menu(self.canvas)
					self.window.blit(self.canvas, (0,0))
					pygame.display.update()
					self.curr_menu.reset_keys()
					self.curr_menu.menu_touch.reset_touch()
					self.curr_menu.reset_fingers()

			
			self.ESCAPE = False
			self.touch_idle.reset_touch()
					
	def Eat(self, food):
		self.house = pygame.image.load('../assets/backgrounds/kitchen.png')
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
					if  self.curr_menu.mini_menu_change:
						self.curr_menu = MiniMenu()
						self.curr_menu.mini_menu_change = False
					if self.curr_menu.mini_water_loop_change:
						self.curr_menu.menu_running = False
						self.eating_running = False
						self.mini_water_flag = True
						self.curr_menu.mini_water_loop_change = False
					self.curr_menu.check_events(self.curr_menu.menu_touch)
					self.curr_menu.display_menu(self.canvas)
					self.window.blit(self.canvas, (0,0))
					pygame.display.update()
					self.curr_menu.reset_keys()
					self.curr_menu.menu_touch.reset_touch()
					self.curr_menu.reset_fingers()
	
			self.window.blit(self.canvas, (0,0))
			pygame.display.update()	
			self.poke.reset_keys()

	def water_mini(self):
		self.reset_fingers()
		self.water = pygame.image.load('../assets/backgrounds/water.png')
		self.water_jet = pygame.image.load('test water jet.png')
		self.water_character = WaterCharacter()
		self.magicarp = Magicarp()
		self.waterjets = []
		self.current_score = 0
		self.water_hud = WaterHud()
		self.distance_triggered = False
		self.mini_touch = FullTouch()
		
		while self.water_mini_running:
			self.clock.tick(60)
			if self.distance_triggered == False:
				self.check_events(self.mini_touch)
				if self.LEFT_KEY:
					self.water_character.move_left()
				elif self.RIGHT_KEY:
					self.water_character.move_right()
				if self.SPACE:
					self.waterjets.append([self.water_character.rect.centerx, self.water_character.rect.y] )

				for waterjet in self.waterjets:
					waterjet[1] -= 10
					if waterjet[1] < 0 :
						self.waterjets.remove(waterjet)
					elif waterjet[0] in range(self.magicarp.rect.centerx - 20, self.magicarp.rect.centerx + 20) and waterjet[1] in range (self.magicarp.rect.centery - 20, self.magicarp.rect.centery + 5):
						self.magicarp.state = 'death'
						self.waterjets.remove(waterjet)
						self.current_score += 1

				if self.magicarp.rect.bottom <= 320 and self.magicarp.state != 'death':
					self.magicarp.move_forward()
				elif self.magicarp.rect.bottom > 320:
					self.distance_triggered = True
				
				self.canvas.blit(self.water, (0,0))
				for waterjet in self.waterjets:
					self.canvas.blit(self.water_jet, waterjet)
				self.magicarp.animation()
				self.magicarp.draw(self.canvas)
				self.water_character.draw(self.canvas)
				self.water_hud.hud_update(self.canvas, self.current_score)
				self.mini_touch.touch_draw(self.canvas)
				self.window.blit(self.canvas, (0,0))
				pygame.display.update()

				self.SPACE = False
				self.mini_touch.reset_touch()
				
			else:
				while self.magicarp.smacked == False:
					self.check_events()
					self.magicarp.smack_player(self.water_character.rect.centerx, self.water_character.rect.top)
					self.canvas.blit(self.water, (0,0))
					self.water_character.draw(self.canvas)
					self.magicarp.draw(self.canvas)
					self.clock.tick(120)
					self.window.blit(self.canvas, (0,0))
					pygame.display.update()
				else:
					self.reset_keys()
					if self.water_high_score < self.current_score:
						self.water_high_score = self.current_score
					self.curr_menu = PostWaterMenu()
					self.water_hud.lose_screen(self.canvas, self.current_score, self.water_high_score)
					while self.curr_menu.menu_running:
						self.curr_menu.check_events(self.curr_menu.menu_touch)
						self.curr_menu.display_menu(self.canvas)
						self.window.blit(self.canvas, (0,0))
						pygame.display.update()
						self.curr_menu.reset_keys()
						self.curr_menu.menu_touch.reset_touch()
						self.curr_menu.reset_fingers()
						if self.curr_menu.play_loop_change:
							self.curr_menu.play_loop_change = False
							self.play_flag = True
							self.curr_menu.menu_running = False
							self.water_mini_running = False
						elif self.curr_menu.mini_water_loop_change:
							self.curr_menu.mini_water_loop_change = False
							self.mini_water_flag = True
							self.curr_menu.menu_running = False
							self.water_mini_running = False