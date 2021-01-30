import pygame
import os.path

class Touch():
    def __init__(self):
        self.UP, self.DOWN, self.LEFT, self.RIGHT, self.A, self.B, self.MENU_BUTTON = False, False, False, False, False, False, False

    def reset_touch(self):
        self.UP, self.DOWN, self.LEFT, self.RIGHT, self.A, self.B, self.MENU_BUTTON = False, False, False, False, False, False, False

class PartialTouch(Touch):
    def __init__(self):
        Touch.__init__(self)
        self.menu_button = pygame.image.load('../assets/touch_buttons/menu button.png').convert_alpha()
        
        self.menu_button_x_offset, self.menu_button_y_offset = 650, 400
        
        self.menu_button_rect = self.menu_button.get_rect()

    def touch_draw(self, display):
        display.blit(self.menu_button, (self.menu_button_x_offset, self.menu_button_y_offset))

    def touch_input(self, finger):
        
        if finger['x'] > (self.menu_button_rect.left + self.menu_button_x_offset) and finger['x'] < (self.menu_button_rect.right + self.menu_button_x_offset):
            if finger['y'] > (self.menu_button_rect.top + self.menu_button_y_offset) and finger['y'] < (self.menu_button_rect.bottom + self.menu_button_x_offset): 
                self.MENU_BUTTON = True      

class FullTouch(Touch):

    def __init__(self):
        Touch.__init__(self)
        self.a_button =  pygame.image.load('../assets/touch_buttons/A button.png').convert_alpha()
        self.a_button =  pygame.transform.scale(self.a_button, (int(self.a_button.get_size()[0]*.65), int(self.a_button.get_size()[0]*.65)))

        self.b_button =  pygame.image.load('../assets/touch_buttons/B button.png').convert_alpha()
        self.b_button =  pygame.transform.scale(self.b_button, (int(self.b_button.get_size()[0]*.65), int(self.b_button.get_size()[0]*.65)))

        self.dpad = pygame.image.load('../assets/touch_buttons/dpad.png').convert_alpha()
        self.dpad =  pygame.transform.scale(self.dpad, (int(self.dpad.get_size()[0]*.65), int(self.dpad.get_size()[0]*.65)))

        self.a_button_x_offset, self.a_button_y_offset = 725, 375
        self.b_button_x_offset, self.b_button_y_offset = 640, 400
        self.dpad_x_offset, self.dpad_y_offset = 15, 350

        self.a_button_rect = self.a_button.get_rect()
        self.a_button_rect.x, self.a_button_rect.y = self.a_button_x_offset, self.a_button_y_offset

        self.b_button_rect = self.b_button.get_rect()
        self.b_button_rect.x, self.b_button_rect.y = self.b_button_x_offset, self.b_button_y_offset

        self.dpad_rect = self.dpad.get_rect()

    def touch_draw(self, display):
        display.blit(self.a_button, (self.a_button_x_offset, self.a_button_y_offset))
        display.blit(self.b_button, (self.b_button_x_offset, self.b_button_y_offset))
        display.blit(self.dpad, (self.dpad_x_offset, self.dpad_y_offset))

    def touch_input(self, finger):

        if (self.dpad_rect.left + self.dpad_x_offset + self.dpad_rect.width / 3) <= finger['x'] <= (self.dpad_rect.right + self.dpad_x_offset - self.dpad_rect.width / 3):
            if (self.dpad_rect.top + self.dpad_y_offset ) <= finger['y'] <= (self.dpad_rect.top + self.dpad_y_offset + self.dpad_rect.height / 3):
                self.UP = True
                
            elif(self.dpad_rect.bottom + self.dpad_y_offset - self.dpad_rect.height / 3) <= finger['y'] <= (self.dpad_rect.bottom + self.dpad_y_offset):
                self.DOWN = True
                
        elif(self.dpad_rect.top + self.dpad_y_offset + self.dpad_rect.height / 3) <= finger['y'] <= (self.dpad_rect.bottom + self.dpad_y_offset - self.dpad_rect.height / 3):
            if (self.dpad_rect.left + self.dpad_x_offset) <= finger['x'] <= (self.dpad_rect.left + self.dpad_x_offset + self.dpad_rect.width / 3):
                self.LEFT = True
              
            elif(self.dpad_rect.right + self.dpad_x_offset - self.dpad_rect.width / 3) <= finger['x'] <= (self.dpad_rect.right + self.dpad_x_offset):
                self.RIGHT = True
               
        if (self.a_button_rect.left) <= finger['x'] <= (self.a_button_rect.right):
            if (self.a_button_rect.top) <= finger['y'] <= (self.a_button_rect.bottom):
                self.A = True

        elif (self.b_button_rect.left) <= finger['x'] <= (self.b_button_rect.right):
            if (self.b_button_rect.top) <= finger['y'] <= (self.b_button_rect.bottom):
                self.B = True