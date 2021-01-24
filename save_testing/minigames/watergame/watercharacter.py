import pygame

class WaterCharacter():
    def __init__(self):
        self.character = pygame.image.load('test water character.png')
        self.rect = self.character.get_rect()
        self.rect.midbottom = (400, 455)

    def draw(self, display):
        """ Draw the characters current frame onto the window"""
        display.blit(self.character, self.rect) 

    def move_left(self):
        
        if self.rect.left > 10:
            self.rect.x -= 7

    def move_right(self):

        if self.rect.right < 790:
            self.rect.x += 7

