# Description: The test block object
# Author: Jacob Maughan

# Lib Imports
import pygame

class TestBlock():
    def __init__(self, x, y, width, height, window):
        # Init
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window

        # Personalized
        self.ID = 'Enemy'
        self.hit = False

        # Collision
        self.collider = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def tick(self, ticks):
        pass

    def render(self, scrollX, scrollY):
        # Render block
        if self.hit == False:
            self.window.drawRect(self.x - scrollX, self.y - scrollY, self.width, self.height, 0, 255, 0)
        if self.hit == True:
            self.window.drawRect(self.x - scrollX, self.y - scrollY, self.width, self.height, 255, 0, 0)