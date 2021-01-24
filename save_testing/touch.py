import pygame
import os.path


class GameTouch():
    def __init__(self):
        self.menu_button = pygame.image.load('assets/touch_buttons/menu button.png').convert_alpha()
        
        self.menu_button_x_offset, self.menu_button_y_offset = 650, 400
        
        self.menu_button_rect = self.menu_button.get_rect()

    def touch_gameloop_draw(self, display):
        display.blit(self.menu_button, (self.menu_button_x_offset, self.menu_button_y_offset))

    def touch_gameloop_checkinput(self, x, y):
        if x > ((self.menu_button_rect.left + self.menu_button_x_offset) / 800) and x < ((self.menu_button_rect.right + self.menu_button_x_offset) / 800):
            if y > ((self.menu_button_rect.top + self.menu_button_y_offset) / 480) and y < ((self.menu_button_rect.bottom + self.menu_button_x_offset) / 480): 
                return "menu button pressed"   
        
class MenuTouch():
    def __init__(self):
        self.a_button =  pygame.image.load('assets/touch_buttons/A button.png').convert_alpha()
        self.b_button =  pygame.image.load('assets/touch_buttons/B button.png').convert_alpha()
        self.dpad = pygame.image.load('assets/touch_buttons/dpad.png').convert_alpha()

        self.a_button_x_offset, self.a_button_y_offset = 675, 325
        self.b_button_x_offset, self.b_button_y_offset = 550, 375
        self.dpad_x_offset, self.dpad_y_offset = 30, 300

        self.a_button_rect = self.a_button.get_rect()
        self.b_button_rect = self.b_button.get_rect()
        self.dpad_rect = self.dpad.get_rect()

    def touch_menuloop_draw(self, display):
        display.blit(self.a_button, (self.a_button_x_offset, self.a_button_y_offset))
        display.blit(self.b_button, (self.b_button_x_offset, self.b_button_y_offset))
        display.blit(self.dpad, (self.dpad_x_offset, self.dpad_y_offset))

    def touch_menuloop_checkinput(self, x, y):
        if x > ((self.a_button_rect.left + self.a_button_x_offset) / 800) and x < ((self.a_button_rect.right + self.a_button_x_offset) / 800):
            if y > ((self.a_button_rect.top + self.a_button_y_offset) / 480) and y < ((self.a_button_rect.bottom + self.a_button_x_offset) / 480): 
                return "a button pressed"   

        elif x > ((self.b_button_rect.left + self.b_button_x_offset) / 800) and x < ((self.b_button_rect.right + self.b_button_x_offset) / 800):
            if y > ((self.b_button_rect.top + self.b_button_y_offset) / 480) and y < ((self.b_button_rect.bottom + self.b_button_x_offset) / 480): 
                return "b button pressed"

        elif ((self.dpad_rect.left + self.dpad_x_offset + self.dpad_rect.width / 3) /800) <= x <= ((self.dpad_rect.right + self.dpad_x_offset - self.dpad_rect.width / 3)/800):
            if ((self.dpad_rect.top + self.dpad_y_offset )/480) <= y <= ((self.dpad_rect.top + self.dpad_y_offset + self.dpad_rect.height / 3)/480):
                return "up"
            elif((self.dpad_rect.bottom + self.dpad_y_offset - self.dpad_rect.height / 3)/ 480) <= y <= ((self.dpad_rect.bottom + self.dpad_y_offset)):
                return "down"

        elif((self.dpad_rect.top + self.dpad_y_offset + self.dpad_rect.height / 3) / 480) <= y <= ((self.dpad_rect.bottom + self.dpad_y_offset - self.dpad_rect.height / 3) / 480):
            if ((self.dpad_rect.left + self.dpad_x_offset) / 800) <= x <= ((self.dpad_rect.left + self.dpad_x_offset + self.dpad_rect.width / 3) / 800):
                return "left"
            elif((self.dpad_rect.right + self.dpad_x_offset - self.dpad_rect.width / 3) / 800) <= x <= ((self.dpad_rect.right + self.dpad_x_offset) / 800):
                return "right"