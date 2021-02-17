# Description: The tile object
# Author: Jacob Maughan

# Lib Imports
import pygame

class Tile():
    def __init__(self, x, y, width, height, sprite, hasCollision, window):
        # Init
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprite = sprite
        self.hasCollision = hasCollision
        self.window = window

        # Personalized
        self.ID = 'Tile'

        # Collision
        self.collider = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def tick(self, ticks):
        pass

    def render(self, scrollX, scrollY):
        # Render tile
        self.window.drawSprite(self.x - scrollX, self.y - scrollY, self.width, self.height, self.sprite)