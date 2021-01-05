import pygame

class Animations():
    def __init__(self):
        self.current_frame = 0
        self.last_updated_animated_time = 0

    def eat(self, display, background, character):
        while self.current_frame < (len(character.eating_frames) - 1):
            now = pygame.time.get_ticks()
            if now - self.last_updated_animated_time > 200:
                self.last_updated_animated_time = now  
                display.blit(background, (0,0))
                display.blit(character.eating_frames[self.current_frame], (350,225))
                self.current_frame +=1
                pygame.display.update()
                print(self.current_frame)
                

  

