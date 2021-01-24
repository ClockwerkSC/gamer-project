from spritesheet import Spritesheet
import pygame

class Food():
    def __init__(self, foodname):
        self.foodfile = f'assets/food/{foodname}'
        food_spritesheet = Spritesheet(self.foodfile)
        self.food_frames = food_spritesheet.get_frames()
        self.last_updated_food_time = 0
        self.current_frame = 0
        self.current_image = self.food_frames[0]
        self.rect = self.food_frames[0].get_rect()
        self.rect.midbottom = (415, 325)
        

    def foodanimation(self):
        now = pygame.time.get_ticks()
        if now - self.last_updated_food_time > 300:
                self.last_updated_food_time = now
                
                if self.current_frame < (len(self.food_frames)):
                    self.current_image = self.food_frames[self.current_frame]
                    self.rect = self.current_image.get_rect()
                    self.current_frame +=1
                    self.rect.midbottom = (415, 325)
                

    def reset(self):
        self.current_frame = 0

    def fooddraw(self, display):
        self.foodanimation()
        """ Draw the characters current frame onto the window"""
        display.blit(self.current_image, self.rect)
        