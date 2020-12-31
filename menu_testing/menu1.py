import pygame

class Menu():
	def __init__(self):
		self.font_name = "Pokemon Classic.TTF"
		self.xpos, self.ypos, = 650, 240
		self.run_menu = True
		self.cursor_rect = pygame.Rect(0, 0, 20, 20)
		self.offset = - 50
		self.background = pygame.image.load('backgrounds/menu background.png').convert_alpha()
		self.curr_menu = MainMenu(self)
	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running, self.playing = False, False
				self.curr_menu.run_display = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					self.START_KEY = True
				if event.key == pygame.K_BACKSPACE:
					self.BACK_KEY = True
				if event.key == pygame.K_DOWN:
					self.DOWN_KEY = True
				if event.key == pygame.K_UP:
					self.UP_KEY = True

	def draw_text(self, text, size, x, y):
		font = pygame.font.Font(self.font_name,size)
		text_surface = font.render(text, True, (0, 0, 0))
		text_rect = text_surface.get_rect()
		text_rect.center = (x,y)
		self.display.blit(text_surface, text_rect)
	def draw_cursor(self):
		self.draw_text('>', 15, self.cursor_rect.x, self.cursor_rect.y)

	def blit_screen(self):
		self.window.blit(self.display, (0,0))
		pygame.display.update()
		self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

class MainMenu(Menu):
	def __init__(self, game):
		self.state = "Eat"
		self.eatx, self.eaty = self.xpos, self.ypos - 220
		self.playx, self.playy = self.xpos, self.ypos - 200
		self.bathroomx, self.bathroom = self.xpos, self.ypos - 180
		self.wardrobex, self.wardrobey = self.xpos, self.ypos -160
		self.townx, self.towny, = self.xpos, self.ypos - 140
		self.choosepokex, self.choosepokey = self.xpos, self.ypos - 120
		self.minigamesx, self.minigamesy = self.xpos, self.ypos - 100
		self.cursor_rect.left = self.eatx + self.offset, self.eaty

	def display_menu(self):

		self.run_display = True
		while self.run_display:
			self.check_events()
			self.check_input()
			self.display.blit(self.background, (0,0)) 
			self.draw_text('Menu', 20, self.xpos, self.ypos - 240)
			self.draw_text('Eat', 20, self.eatx, self.eaty)
			self.draw_text('Play', 20, self.playx, self.playy)
			self.draw_text('Bathroom', 20, self.bathroomx, self.bathroomy)
			self.draw_text('Wardrobe', 20, self.wardrobex, self.wardrobey)
			self.draw_text('Town', 20, self.townx, self.towny)
			self.draw_text('Choose Pokemon', 20, self.choosepokex, self.choosepokey)
			self.draw_text('Mini Games', 20, self.minigamesx, self.minigamesy)
			self.draw_cursor()
			self.blit_screen()

	def move_cursor(self):

		if self.DOWN_KEY:
			if self.state == 'Eat':
				self.cursor_rect.left = (self.playx + self.offset, self.playy)
				self.state = 'Play'
			elif self.state == 'Play':
				self.cursor_rect.left = (self.bathroomx	+ self.offset, self.bathroomy)
				self.state = 'Bathroom'
			elif self.state == 'Bathroom':
				self.cursor_rect.left = (self.wardrobex + self.offset, self.wardrobey)
				self.state = 'Wardrobe'
			elif self.state == 'Wardrobe':
				self.cursor_rect.left = (self.towny + self.offset, self.towny)
				self.state = 'Choose Pokemon'
			elif self.state == 'Choose Pokemon':
				self.cursor_rect.left = (self.minigamesx + self.offset, self.minigamesy)
				self.state = 'Mini Games'
			elif self.state == 'Mini Games':
				self.cursor_rect.left = (self.eatx + self.offset, self.eaty)


		if self.UP_KEY:
			if self.state == 'Eat':
				self.cursor_rect.left = (self.minigamesx + self.offset, self.minigamesy)
				self.state = 'Mini Games'
			elif self.state == 'Choose Pokemon':
				self.cursor_rect.left = (self.wardrobex + self.offset, self.wardrobey)
				self.state = 'Wardrobe'
			elif self.state == 'Wardrobe':
				self.cursor_rect.left = (self.bathroomx + self.offset, self.bathroomy)
				self.state = 'Bathroom'
			elif self.state == 'Bathroom':
				self.cursor_rect.left = (self.playx +self.offset, self.playy)
				self.state = 'Play'
			elif self.state == 'Play':
				self.cursor_rect.left = (self.eatx + self.offset, self.eaty)
			elif self.state == 'Mini Games':
				self.cursor_rect.left = (self.choosepokex + self.offset, self.choosepokey)
				self.state = 'Choose Pokemon'
