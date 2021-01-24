import pygame
import math
import random

class Magicarp():
    def __init__(self):
        self.magicarp = pygame.image.load('test magicarp.png')
        self.rect = self.magicarp.get_rect()
        self.rect.midbottom = [random.randint(30, 770), random.randint(0, 40)]
        self.speed = 4
        self.smacked = False

    def get_new_position(self):
        self.rect.midbottom = [random.randint(30, 770), random.randint(0, 40)]

    def move_forward(self):
        self.rect.y += 2

    def draw(self, display):
        """ Draw the characters current frame onto the window"""
        display.blit(self.magicarp, self.rect) 

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