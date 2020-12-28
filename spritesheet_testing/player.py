import random
import pygame
from spritesheet import Spritesheet

class Player(pygame.sprite.Sprite):
    def __init__(self, spritesheet_name):
        pygame.sprite.Sprite.__init__(self)
        p_spritesheet = {'totodile': 'character_spritesheets/Totodile Art.png',
            'croconaw': 'character_spritesheets/Croconaw Art.png',
            'feraligatr': 'character_spritesheets/Feraligatr Art.png',
            'cyndaquil': 'character_spritesheets/Cyndaquil Art.png',
            'quilava': 'character_spritesheets/Quilava Art.png',
            'typhlosion': 'character_spritesheets/Typhlosion Art.png',
            'chikorita': 'character_spritesheets/Chikorita Art.png',
            'bayleef': 'character_spritesheets/Bayleef Art.png',
            'meganium': 'character_spritesheets/Meganium Art.png',
            }


        self.sname = p_spritesheet[spritesheet_name.lower()]
        self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT = False, False, False
        self.load_frames()
        self.rect = self.idle_frames_left[0].get_rect()
        self.rect.midbottom = (240, 450)
        self.current_frame = 0
        self.last_updated = 0
        self.velocity = 0
        self.state = 'idle'
        self.current_image = self.idle_frames_left[0]


    def draw(self, display):
        display.blit(self.current_image, self.rect)    

    def update(self):
        self.velocity = 0  ####Code for User Controlled Poppy
        if self.LEFT_KEY and self.rect.left > 0:
            self.velocity = -2
        elif self.RIGHT_KEY and self.rect.right < 800:
            self.velocity = 2
        self.rect.x += self.velocity
        self.set_state()
        self.animate() 
        

    def set_state(self):
         self.state = 'idle'
         if self.velocity > 0:
            self.state = 'moving right'
         elif self.velocity < 0:
            self.state = 'moving left' 

    def animate(self):
        now = pygame.time.get_ticks()
        if self.state == 'idle':
            if now - self.last_updated > 200:
                self.last_updated = now  
                self.current_frame = (self.current_frame +1) % len(self.idle_frames_left) 
                if self.FACING_LEFT:
                    self.current_image = self.idle_frames_left[self.current_frame]
                elif not self.FACING_LEFT:
                    self.current_image = self.idle_frames_right[self.current_frame]
        else:
            if now - self.last_updated > 100:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_frames_left)
                if self.state == 'moving left':
                    self.current_image = self.walking_frames_left[self.current_frame]
                elif self.state == 'moving right':
                    self.current_image = self.walking_frames_right[self.current_frame]
        self.x_now, self.y_now = self.rect.bottomleft
        self.rect = self.current_image.get_rect()
        self.rect.bottom = 450
        self.rect.bottomleft = self.x_now, self.y_now

    def load_frames(self):  
        my_spritesheet = Spritesheet(self.sname)
        self.idle_frames_right, self.walking_frames_right = my_spritesheet.get_frames()
        self.idle_frames_left = []
        for frame in self.idle_frames_right:
            self.idle_frames_left.append(pygame.transform.flip(frame, True, False))
        self.walking_frames_left = []
        for frame in self.walking_frames_right:
            self.walking_frames_left.append(pygame.transform.flip(frame, True, False))


















