# Description: The tile object
# Author: Jacob Maughan

# Lib Imports
import pygame

class Tile():
    def __init__(self, x, y, width, height, hasCollision, window):
        # Init
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hasCollision = hasCollision
        self.window = window

        self.ID = 'Tile'

        self.collider = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def tick(self, ticks):
        pass

    def render(self, scrollX, scrollY):
        # Render tile
        self.window.drawRect(self.x - scrollX, self.y - scrollY, self.width, self.height, 255, 0, 0)