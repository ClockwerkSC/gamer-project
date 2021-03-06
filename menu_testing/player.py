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
        self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT, self.SPACE, self.BACK, self.Q, self.Z = False, False, False, False, False, False, False
        self.load_frames()
        self.rect = self.idle_frames_left[0].get_rect()
        self.rect.midbottom = (240, 450)
        self.current_frame = 0
        self.last_updated_animated_time = 0
        self.velocity = 0
        self.state = 'idle'
        self.current_image = self.idle_frames_left[0]
        self.experience = 0
        self.xp_max = 200
        self.level = 0
        self.name = "George"
        self.happiness = 200
        self.happiness_max = 200
        self.hunger = 200
        self.hunger_max = 200
        self.last_updated_happiness_time = 0
        self.last_updated_hunger_time = 0
        self.ai_duration = 0

    def draw(self, display):
        """ Draw the characters current frame onto the window"""
        display.blit(self.current_image, self.rect) 
         
    def update(self):
        """Change the velocity of the character based on user input.
        The position of the character is updated, and the character attributes are updated.
        """
        #### Code for moving Poke manually ###
        # self.velocity = 0   
        # if self.LEFT_KEY and self.rect.left > 0:
        #     self.velocity = -2
        # elif self.RIGHT_KEY and self.rect.right < 800:
        #     self.velocity = 2

        # Radomly assign AI movement for character
        if self.ai_duration <= 0:
            self.get_ai_duration()
        self.ai_duration -=1

        self.rect.x += self.velocity
        self.set_state()
        self.animate()
        self.increase_xp() 
        self.happiness_update()
        self.hunger_update()
        
    def get_ai_duration(self):
        """Character is randomly assigned to walk left, walk right, or wait for a random period of time"""
        self.ai_duration = random.randint(10,100)
        self.velocity = random.choice([1,0, 0, 0, 0, 0, -1])
        if self.velocity == -1:
            self.FACING_LEFT = True
        if self.velocity == 1:
            self.FACING_LEFT = False

    def set_state(self):
        """Change to the correct animation sequence based on motion of the character"""
        self.state = 'idle'
        if self.velocity > 0:
            self.state = 'moving right'
        elif self.velocity < 0:
            self.state = 'moving left' 

    def animate(self):
        """Select the correct frame in the animation sequence based on the current state
        of the character every specified amount of time in milliseconds
        """
        now = pygame.time.get_ticks()
        if self.state == 'idle':
            if now - self.last_updated_animated_time > 200:
                self.last_updated_animated_time = now  
                self.current_frame = (self.current_frame +1) % len(self.idle_frames_left) 
                if self.FACING_LEFT:
                    self.current_image = self.idle_frames_left[self.current_frame]
                elif not self.FACING_LEFT:
                    self.current_image = self.idle_frames_right[self.current_frame]
        else:
            if now - self.last_updated_animated_time > 100:
                self.last_updated_animated_time = now
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
        """load the frames from the spritesheets and create animations sequences for opposite direction"""  
        my_spritesheet = Spritesheet(self.sname)
        self.idle_frames_right, self.walking_frames_right = my_spritesheet.get_frames()
        self.idle_frames_left = []
        for frame in self.idle_frames_right:
            self.idle_frames_left.append(pygame.transform.flip(frame, True, False))
        self.walking_frames_left = []
        for frame in self.walking_frames_right:
            self.walking_frames_left.append(pygame.transform.flip(frame, True, False))

    def increase_xp(self):
        """Increase the XP bar: currently increased when space bar is hit"""
        if self.SPACE:
            if self.experience < self.xp_max:
                self.experience += 1
            elif self.experience >= self.xp_max:
                self.experience = 0
                self.level += 1

    def happiness_update(self):
        """Naturally decrease happiness meter over time and increase hunger meter when feeding condition is met"""
        now = pygame.time.get_ticks()
        if now - self.last_updated_happiness_time > 500 and self.happiness > 0:
            self.last_updated_happiness_time = now
            self.happiness -= 10
            if self.happiness <= 0:
                self.happiness = 0
        if self.Q and self.happiness < self.happiness_max:
            self.happiness += 5
            if self.happiness > self.happiness_max:
                self.happiness = self.happiness_max


    def hunger_update(self):
        """Naturally decrease hunger meter over time and increase hunger meter when feeding condition is met"""
        now = pygame.time.get_ticks()
        if now - self.last_updated_hunger_time > 500 and self.hunger > 0:
            self.last_updated_hunger_time = now
            self.hunger -= 10
            if self.hunger <= 0:
                self.hunger = 0
        if self.Z and self.hunger < self.hunger_max:
            self.hunger += 5
            if self.hunger > self.hunger_max:
                self.hunger = self.hunger_max

    











