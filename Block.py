# Description: The block object
# Author: Jacob Maughan

# Lib Imports
import pygame

class Block():
    def __init__(self, x, y, width, height, window):
        # Init
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window

        self.ID = 'Block'

        self.collider = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def tick(self, ticks):
        pass

    def render(self, scrollX, scrollY):
        # Render block
        self.window.drawRect(self.x - scrollX, self.y - scrollY, self.width, self.height, 255, 0, 0)