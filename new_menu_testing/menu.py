import pygame
from hud import Hud

class Menu():
    def __init__(self):
        self.menu_background = pygame.image.load('backgrounds/menu background.png').convert_alpha()
        self.menu_running = True
        self.START_KEY, self.BACK_KEY, self.UP_KEY, self.DOWN_KEY = False, False, False, False
        self.state = 'MAIN'


    def check_events(self):
        """ Check for key presses and set appropriate flags"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.menu_running = False
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True    
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
            if event.type == pygame.KEYUP:    
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = False
                if event.key == pygame.K_UP:
                    self.UP_KEY = False
    def draw_text(self, display, text, size, x, y , mode):
        """Create text surface and blit onto another display surface.
        There is an option to scpecifiy the location by center or topleft corner
        """
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (0,0,0))
        text_rect = text_surface.get_rect()
        if mode == "left":
            text_rect.topleft = (x,y)
        elif mode == "center":
            text_rect.center = (x,y)
        display.blit(text_surface, text_rect)

    def draw_cursor(self, display):
        self.draw_text(display, '>', 10, self.pos_dict[self.current_key][0] - 10, self.pos_dict[self.current_key][1], "left")
        print(self.i)

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY = False, False  

class MainMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.font_name = "Pokemon Classic.TTF"
        self.icons = ['EAT', 'PLAY', 'BATHROOM', 'WARDROBE', 'TOWN', 'CHOOSE POKE', 'MINI GAMES']
        self.eatx, self.eaty = 660, 10
        self.playx, self.playy = 660, 30
        self.bathroomx, self.bathroomy = 660, 50
        self.wardrobex, self.wardrobey = 660, 70
        self.townx, self.towny = 660, 90
        self.choosepokex, self.choosepokey = 660, 110
        self.minix, self.miniy = 660, 130
        #self.state = 'EAT'
        self.current_key = self.icons[0]
        self.i = 0

        self.pos_dict = {'EAT': (self.eatx, self.eaty),
            'PLAY': (self.playx, self.playy),
            'BATHROOM':(self.bathroomx, self.bathroomy),
            'WARDROBE':(self.wardrobex, self.wardrobey),
            'TOWN':(self.townx, self.towny),
            'CHOOSE POKE':(self.choosepokex, self.choosepokey),
            'MINI GAMES':(self.minix, self.miniy)}

    def draw_text(self, display, text, size, x, y , mode):
        """Create text surface and blit onto another display surface.
        There is an option to scpecifiy the location by center or topleft corner
        """
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (0,0,0))
        text_rect = text_surface.get_rect()
        if mode == "left":
            text_rect.topleft = (x,y)
        elif mode == "center":
            text_rect.center = (x,y)
        display.blit(text_surface, text_rect)

    def display_menu(self, display):
        """Display main menu"""
        display.blit(self.menu_background, (650,0))
        for icon in self.icons:
            self.draw_text(display, icon, 10, *self.pos_dict[icon], "left")
        self.move_cursor(display)
        self.draw_cursor(display)
    def move_cursor(self, display):
        
        if self.DOWN_KEY:
            self.i = self.i + 1
            if self.i > 6:
                self.i = 0
            self.current_key = self.icons[self.i]
        self.DOWN_KEY = False
        if self.UP_KEY:
            self.i = self.i-1
            if self.i < 0:
                self.i = 6
            self.current_key = self.icons[self.i]
        if self.START_KEY == True:
            self.state = self.icons[self.i]


class EatMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.font_name = "Pokemon Classic.TTF"
        self.icons = ['SNACK', 'MEAL']
        #self.state = 'SNACK'
        self.current_key = self.icons[0]
        self.i = 0
        self.snackx, self.snacky = 660, 10
        self.mealx, self.mealy = 660, 30

        self.pos_dict = {'SNACK': (self.snackx, self.mealy),
            'MEAL': (self.mealx, self.mealy)}

    def draw_text(self, display, text, size, x, y , mode):
        """Create text surface and blit onto another display surface.
        There is an option to scpecifiy the location by center or topleft corner
        """
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (0,0,0))
        text_rect = text_surface.get_rect()
        if mode == "left":
            text_rect.topleft = (x,y)
        elif mode == "center":
            text_rect.center = (x,y)
        display.blit(text_surface, text_rect)

    def display_menu(self, display):
        """Display main menu"""
        display.blit(self.menu_background, (650,0))
        for icon in self.icons:
            self.draw_text(display, icon, 10, *self.pos_dict[icon], "left")
        self.move_cursor(display)
        self.draw_cursor(display)
    def move_cursor(self, display):
        
        if self.DOWN_KEY:
            self.i = self.i + 1
            if self.i > 6:
                self.i = 0
            self.current_key = self.icons[self.i]
        self.DOWN_KEY = False
        if self.UP_KEY:
            self.i = self.i-1
            if self.i < 0:
                self.i = 6
            self.current_key = self.icons[self.i]






           