import pygame
from hud import Hud

class Menu():
    def __init__(self):
        self.menu_background = pygame.image.load('backgrounds/menu background.png').convert_alpha()
        self.menu_running = True
        self.START_KEY, self.BACK_KEY, self.UP_KEY = False, False, False


    def check_events(self):
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

class MainMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.icons = ['Eat', 'play', 'bathroom']
        self.eatx, self.eaty = 660, 10
        self.playx, self.playy = 660, 30
        self.bathroomx, self.bathroomy = 660, 50

        self.pos_dict = {'Eat': (self.eatx, self.eaty),
            'play': (self.playx, self.playy),
            'bathroom':(self.bathroomx, self.bathroomy)}

    def draw_text(self, display, text, size, (x,y), mode):
        """Create text surface and blit onto another display surface.
        There is an option to scpecifiy the location by center or topleft corner
        """
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (0,0,0))
        text_rect = text_surface.get_rect()
        if mode == "left":
            text_rect.topleft = (x,y)
        elif mode == "center":
            text_rect.center = (x, y)
        display.blit(text_surface, text_rect)

    def display_menu(self, display):
        display.blit(self.menu_background, (650,0))
        for icon in self.icons:
            self.draw_text(display, icon, 10, *self.pos_dict[icon], "left")


           