import pygame

class Hud():
    def __init__(self):
        self.font_name = "assets/fonts/Pokemon Classic.TTF"
         #Setting geometries for the HUD
        self.HUD_width = 450
        self.blank_HUD_background = pygame.image.load('assets/HUD/blank hud background.png').convert_alpha()

        
        

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

    

class DefaultHud(Hud):
    def __init__ (self):
        Hud.__init__(self)
        self.xp_barwidth = 100
        self.xp_levelwidth = 0
        self.happiness_levelwidth = self.xp_barwidth
        self.hunger_levelwidth = self.xp_barwidth
        
        self.xp_bar_x_offset = (self.HUD_width / (3) * 1) - self.xp_barwidth * 1.25
        self.xp_bar_y_offset = 30
        self.happy_bar_x_offset = (self.HUD_width / (3) * 2) - self.xp_barwidth * 1.25
        self.hunger_bar_x_offset = (self.HUD_width / (3) * 3) - self.xp_barwidth * 1.25
        self.status_text_y_offset = self.xp_bar_y_offset - 16
        self.happiness_color = pygame.Color('#33FF41')
        self.hunger_color = pygame.Color('#33FF41')
        self.default_HUD_background = pygame.image.load('assets/HUD/HUD.png').convert_alpha()

    def hud_update(self, display, object):
        """draw and blit all objects necessary to create the HUD""" 
        display.blit(self.default_HUD_background, (0,0)) 

        # Level section of HUD
        self.xp_levelwidth = object.experience * self.xp_barwidth / object.xp_max
        self.xp_level = pygame.draw.rect(display, (0,222,255), (self.xp_bar_x_offset,self.xp_bar_y_offset,self.xp_levelwidth,10)) 
        self.level_text = self.draw_text(display, "Lv", 10 , self.xp_bar_x_offset, self.status_text_y_offset, "left")
        self.level_number = self.draw_text(display, str(object.level), 12, self.xp_bar_x_offset + 20, self.status_text_y_offset - 3, "left")

        # Happiness section of HUD
        if object.happiness > .5 * object.happiness_max:
            self.happiness_color = pygame.Color('#33FF41')
        elif object.happiness < .5 * object.happiness_max and object.happiness > .2 * object.happiness_max:
            self.happiness_color = pygame.Color("#F6FF33")
        elif object.happiness < .2 * object.happiness_max:
             self.happiness_color = pygame.Color("#FF3C33")
        self.happiness_levelwidth = object.happiness * self.xp_barwidth / object.happiness_max
        self.happy_level = pygame.draw.rect(display, self.happiness_color, (self.happy_bar_x_offset,self.xp_bar_y_offset,self.happiness_levelwidth,10))
        self.happy_text = self.draw_text(display, "Happiness", 10 , self.happy_bar_x_offset, self.status_text_y_offset, "left")
        
        # Hunger Section of HUD
        if object.hunger > .5 * object.hunger_max:
            self.hunger_color = pygame.Color('#33FF41')
        elif object.hunger < .5 * object.hunger_max and object.hunger > .2 * object.hunger_max:
            self.hunger_color = pygame.Color("#F6FF33")
        elif object.hunger < .2 * object.hunger_max:
             self.hunger_color = pygame.Color("#FF3C33")
        self.hunger_levelwidth = object.hunger * self.xp_barwidth / object.hunger_max
        self.hunger_level = pygame.draw.rect(display, self.hunger_color, (self.hunger_bar_x_offset,self.xp_bar_y_offset,self.hunger_levelwidth,10))
        self.hunger_text = self.draw_text(display, "Hunger", 10 , self.hunger_bar_x_offset, self.status_text_y_offset, "left")
        self.name_text = self.draw_text(display, object.name, 10, self.xp_bar_x_offset, self.status_text_y_offset - 15, "left")


class WaterHud(Hud):
    def __init__(self):
        Hud.__init__(self)
        self.magicarp_icon = pygame.image.load('test magicarp.png').convert_alpha()
        


    def hud_update(self, display, current_score):
        display.blit(self.blank_HUD_background, (0,0))
        display.blit(self.magicarp_icon, (10, 10))
        self.draw_text(display, str(current_score), 12, 35, 20,  "left")