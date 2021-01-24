import pygame
import math
import random
from spritesheet import Spritesheet

class Magicarp():
    def __init__(self):
        self.file = "../assets/minigame_sprites/magikarp.png" 
        self.magikarp_spritesheet = Spritesheet(self.file)
        self.emerge_frames, self.death_frames, self.swim_frames = self.magikarp_spritesheet.get_frames()
        self.current_frame = 0
        self.current_image = self.swim_frames[0]
        self.rect = self.current_image.get_rect()
        self.rect.midbottom = [random.randint(30, 770), random.randint(40, 70)]
        self.speed = 4
        self.smacked = False
        self.state = 'emerge'
        self.last_updated_time = 0

    def get_new_position(self):
        self.rect.midbottom = [random.randint(30, 770), random.randint(40, 70)]
        self.state = 'emerge'
        self.current_frame = 0

    def move_forward(self):
        self.rect.y += 2

    def draw(self, display):
        """ Draw the characters current frame onto the window"""
        display.blit(self.current_image, self.rect) 

    def smack_player(self, playerx, playery):
        # Find direction vector (dx, dy) between enemy and player.
        dx, dy = playerx - self.rect.centerx, playery - self.rect.centery
        dist = 0
        if abs(dx) <= 0.1:
            dist = dy
        elif abs(dy) <= 0.1:
            dist = dx
        else:
            dist = math.hypot(dx, dy)

        if dist < 1:
            self.smacked = True    
        else:
            dx, dy = dx / dist, dy / dist  # Normalize.
            # Move along this normalized vector towards the player at current speed.
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

    def animation(self):
        if self.state == 'emerge':
            now = pygame.time.get_ticks()
            if now - self.last_updated_time > 30:
                    self.last_updated_time = now
                    if self.current_frame < (len(self.emerge_frames)):
                        self.current_image = self.emerge_frames[self.current_frame]
                        self.oldmidbottom = self.rect.midbottom
                        self.rect = self.current_image.get_rect()
                        self.rect.midbottom  = self.oldmidbottom
                        self.current_frame +=1
                    else: self.state = 'swim'

        elif self.state == 'swim':
            now = pygame.time.get_ticks()
            if now - self.last_updated_time > 200:
                self.last_updated_time = now  
                self.current_frame = (self.current_frame +1) % len(self.swim_frames) 
                self.current_image = self.swim_frames[self.current_frame]
                self.oldmidbottom = self.rect.midbottom
                self.rect = self.current_image.get_rect()
                self.rect.midbottom  = self.oldmidbottom


        elif self.state == 'death':
            now = pygame.time.get_ticks()
            if now - self.last_updated_time > 10:
                    self.last_updated_time = now
                    if self.current_frame < (len(self.death_frames)):
                        self.current_image = self.death_frames[self.current_frame]
                        self.oldmidbottom = self.rect.midbottom
                        self.rect = self.current_image.get_rect()
                        self.rect.midbottom  = self.oldmidbottom
                        self.current_frame +=1
                    else: self.get_new_position()   