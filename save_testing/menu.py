import pygame
from hud import Hud
from touch import FullTouch

class Menu():
    def __init__(self):
        self.DISPLAY_W, self.DISPLAY_H = 800, 480
        self.menu_background = pygame.image.load('../assets/backgrounds/menu background.png').convert_alpha()
        self.font_name = "../assets/fonts/Pokemon Classic.ttf"
        self.menu_running = True
        self.START_KEY, self.BACK_KEY, self.UP_KEY, self.DOWN_KEY = False, False, False, False
        self.curr_menu = 'main'
        self.eat_menu_change = False
        self.mini_menu_change = False
        self.snack_loop_change = False
        self.meal_loop_change = False
        self.main_menu_change = False
        self.play_loop_change = False
        self.mini_water_loop_change = False
        self.menu_touch = FullTouch()
        self.fingers = {}
        
    def check_events(self, touchcontrol = False):
        """ Check for key presses and set appropriate flags"""
        for event in pygame.event.get():

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
                        if touchcontrol.RIGHT:
                            self.RIGHT_KEY = True
                        if touchcontrol.UP:
                            self.UP_KEY = True
                        if touchcontrol.DOWN:
                            self.DOWN_KEY = True

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

    def reset_fingers(self):
        self.fingers = {}

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
        
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY = False, False, False  

    def move_cursor(self, display):
        if self.DOWN_KEY:
            self.i = self.i + 1
            if self.i > len(self.icons) - 1 :
                self.i = 0
            self.current_key = self.icons[self.i]
        if self.UP_KEY:
            self.i = self.i-1
            if self.i < 0:
                self.i = len(self.icons) - 1
            self.current_key = self.icons[self.i]
        if self.START_KEY == True:
            self.state = self.icons[self.i]

    def display_menu(self, display):
        display.blit(self.menu_background, (650,0))
        for icon in self.icons:
            self.draw_text(display, icon, 10, *self.pos_dict[icon], "left")
        self.menu_touch.touch_draw(display)
        self.move_cursor(display)
        self.check_input()
        self.draw_cursor(display)    

class MainMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.icons = ['EAT', 'PLAY', 'BATHROOM', 'WARDROBE', 'TOWN', 'CHOOSE POKE', 'MINI GAMES']
        self.eatx, self.eaty = 660, 10
        self.playx, self.playy = 660, 30
        self.bathroomx, self.bathroomy = 660, 50
        self.wardrobex, self.wardrobey = 660, 70
        self.townx, self.towny = 660, 90
        self.choosepokex, self.choosepokey = 660, 110
        self.minix, self.miniy = 660, 130
        self.current_key = self.icons[0]
        self.i = 0
        self.pos_dict = {'EAT': (self.eatx, self.eaty),
            'PLAY': (self.playx, self.playy),
            'BATHROOM':(self.bathroomx, self.bathroomy),
            'WARDROBE':(self.wardrobex, self.wardrobey),
            'TOWN':(self.townx, self.towny),
            'CHOOSE POKE':(self.choosepokex, self.choosepokey),
            'MINI GAMES':(self.minix, self.miniy)}

    def check_input(self):
        if self.START_KEY:
            if self.state == 'EAT':
                self.curr_menu = "eat menu"
                self.eat_menu_change = True
            elif self.state == 'PLAY':
                self.play_loop_change = True
            elif self.state == 'MINI GAMES':
                self.mini_menu_change = True
        if self.BACK_KEY:
            self.menu_running = False
    
class EatMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.icons = ['SNACK', 'MEAL']
        self.current_key = self.icons[0]
        self.i = 0
        self.snackx, self.snacky = 660, 10
        self.mealx, self.mealy = 660, 30
        self.pos_dict = {'SNACK': (self.snackx, self.snacky),
            'MEAL': (self.mealx, self.mealy)}

    def check_input(self):
        if self.START_KEY:
            if self.state == 'SNACK':
                self.snack_loop_change = True
            elif self.state == 'MEAL':
                self.meal_loop_change = True
        if self.BACK_KEY:
            self.curr_menu = "play menu"
            self.main_menu_change = True

class MiniMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.icons = ['WATER', 'FIRE']
        self.current_key = self.icons[0]
        self.i = 0
        self.waterx, self.watery = 660, 10
        self.firex, self.firey = 660, 30
        self.pos_dict = {'WATER': (self.waterx, self.watery),
            'FIRE': (self.firex, self.firey)}

    def check_input(self):
        if self.START_KEY:
            if self.state == 'WATER':
                self.mini_water_loop_change = True
            elif self.state == 'Fire':
                self.meal_loop_change = True
        if self.BACK_KEY:
            self.main_menu_change = True

class PostWaterMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.icons = ['PLAY AGAIN?', 'EXIT']       
        self.current_key = self.icons[0]
        self.i = 0
        self.playagainx, self.playagainy = 660, 10
        self.exitx, self.exity = 660, 30
        self.pos_dict = {'PLAY AGAIN?': (self.playagainx, self.playagainy),
            'EXIT': (self.exitx, self.exity)}

    def check_input(self):
        if self.START_KEY:
            if self.state == 'PLAY AGAIN?':
                self.mini_water_loop_change = True
            elif self.state == 'EXIT':
                self.play_loop_change = True
        

    