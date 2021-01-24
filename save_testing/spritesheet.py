import pygame
import json

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.meta_data = self.filename.replace('png', 'json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()
        
        self.idle_frames = []
        self.walk_frames = []
        self.passive_kitchen_frames = []
        
        self.eating_frames = []
        self.food_frames = []

        self.emerge_frames = []
        self.death_frames = []
        self.swim_frames = []

    def get_sprite(self, x, y, w, h):
        """Return sprite based of the size and position data grabbed from the json file"""
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((255,0,255))
        sprite.blit(self.sprite_sheet,(0, 0),(x, y, w, h))
        return sprite

    def parse_sprite(self, name):
        """Get the position data from json file. Make a call to get_sprite() to return the sprites"""
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        return image

    def get_frames(self):
        """Automatically get the frames for each animation sequence from the meta data in json file"""

        if 'character' in self.filename:
            for ftag in self.data['frames']:
                if "idle" in ftag.lower():
                    self.idle_frames.append(self.parse_sprite(ftag))
                elif "walk" in ftag.lower():
                    self.walk_frames.append(self.parse_sprite(ftag))
                elif "passive kitchen" in ftag.lower():
                    self.passive_kitchen_frames.append(self.parse_sprite(ftag))
                elif "eating" in ftag.lower():
                    self.eating_frames.append(self.parse_sprite(ftag))
            return self.idle_frames, self.walk_frames, self.passive_kitchen_frames, self.eating_frames

        elif 'food' in self.filename:
            for ftag in self.data['frames']:
                self.food_frames.append(self.parse_sprite(ftag))
            
            return self.food_frames


        elif 'magikarp' in self.filename:
            for ftag in self.data['frames']:
                if "emerge" in ftag.lower():
                    self.emerge_frames.append(self.parse_sprite(ftag))
                elif "death" in ftag.lower():
                    self.death_frames.append(self.parse_sprite(ftag))
                elif "swim" in ftag.lower():
                    self.swim_frames.append(self.parse_sprite(ftag))
            return self.emerge_frames, self.death_frames, self.swim_frames

