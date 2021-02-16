# Description: Handles spritesheets
# Author: Jacob Maughan

# Lib Imports
import pygame

class SpriteSheet():
    def __init__(self, sheet):
        # Init
        self.spriteSheet = pygame.image.load(sheet).convert()
    
    # Get specific sprite from loaded sprite sheet
    def getImage(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.spriteSheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0, 0, 0))
        return image