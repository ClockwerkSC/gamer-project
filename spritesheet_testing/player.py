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
        self.level = 0
        self.font_name = "Pokemon Classic.TTF"
        self.name = "George"
        self.happiness = 200
        self.happiness_max = 200
        self.hunger = 200
        self.hunger_max = 200
        self.last_updated_happiness_time = 0
        self.last_updated_hunger_time = 0
        self.ai_duration = 0

        #Setting geometries for the HUD
        self.HUD_width = 450
        self.xp_barwidth = 100
        self.xp_levelwidth = 0
        self.happiness_levelwidth = self.xp_barwidth
        self.hunger_levelwidth = self.xp_barwidth
        self.xp_bar_max = 200
        self.xp_bar_x_offset = (self.HUD_width / (3) * 1) - self.xp_barwidth * 1.25
        self.xp_bar_y_offset = 30
        self.happy_bar_x_offset = (self.HUD_width / (3) * 2) - self.xp_barwidth * 1.25
        self.hunger_bar_x_offset = (self.HUD_width / (3) * 3) - self.xp_barwidth * 1.25
        self.status_text_y_offset = self.xp_bar_y_offset - 16
        self.HUD_background = pygame.image.load('HUD.png').convert_alpha()
        self.happiness_color = pygame.Color('#33FF41')
        self.hunger_color = pygame.Color('#33FF41')

    def draw(self, display):
        """ Draw the characters current frame and HUD onto the window"""
        display.blit(self.current_image, self.rect) 
        self.hud_update(display) 
        
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
            if self.experience < self.xp_bar_max:
                self.experience += 1
            elif self.experience >= self.xp_bar_max:
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

    def draw_text(self, display, text, size, x, y, mode):
        """Create text surface and blit onto another display surface.
        There is an option to scpecifiy the location by center or topleft corner
        """
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (0,0,0))
        text_rect = text_surface.get_rect()
        if mode == "left":
            text_rect.topleft = (x,y)
        elif mode == "center":
            text_rect.center = (x, y)
        display.blit(text_surface, text_rect)

    def hud_update(self, display):
        """draw and blit all objects necessary to create the HUD""" 
        display.blit(self.HUD_background, (0,0)) 

        # Level section of HUD
        self.xp_levelwidth = self.experience * self.xp_barwidth / self.xp_bar_max
        self.xp_level = pygame.draw.rect(display, (0,222,255), (self.xp_bar_x_offset,self.xp_bar_y_offset,self.xp_levelwidth,10)) 
        self.level_text = self.draw_text(display, "Lv", 10 , self.xp_bar_x_offset, self.status_text_y_offset, "left")
        self.level_number = self.draw_text(display, str(self.level), 12, self.xp_bar_x_offset + 20, self.status_text_y_offset - 3, "left")

        # Happiness section of HUD
        if self.happiness > .5 * self.happiness_max:
            self.happiness_color = pygame.Color('#33FF41')
        elif self.happiness < .5 * self.happiness_max and self.happiness > .2 * self.happiness_max:
            self.happiness_color = pygame.Color("#F6FF33")
        elif self.happiness < .2 * self.happiness_max:
             self.happiness_color = pygame.Color("#FF3C33")
        self.happiness_levelwidth = self.happiness * self.xp_barwidth / self.happiness_max
        self.happy_level = pygame.draw.rect(display, self.happiness_color, (self.happy_bar_x_offset,self.xp_bar_y_offset,self.happiness_levelwidth,10))
        self.happy_text = self.draw_text(display, "Happiness", 10 , self.happy_bar_x_offset, self.status_text_y_offset, "left")
        
        # Hunger Section of HUD
        if self.hunger > .5 * self.hunger_max:
            self.hunger_color = pygame.Color('#33FF41')
        elif self.hunger < .5 * self.hunger_max and self.hunger > .2 * self.hunger_max:
            self.hunger_color = pygame.Color("#F6FF33")
        elif self.hunger < .2 * self.hunger_max:
             self.hunger_color = pygame.Color("#FF3C33")
        self.hunger_levelwidth = self.hunger * self.xp_barwidth / self.hunger_max
        self.hunger_level = pygame.draw.rect(display, self.hunger_color, (self.hunger_bar_x_offset,self.xp_bar_y_offset,self.hunger_levelwidth,10))
        self.hunger_text = self.draw_text(display, "Hunger", 10 , self.hunger_bar_x_offset, self.status_text_y_offset, "left")
        self.name_text = self.draw_text(display, self.name, 10, self.xp_bar_x_offset, self.status_text_y_offset - 15, "left")











