# Description: The sign loader object
# Author: Jacob Maughan

# Lib Imports
import pygame

class Sign():
    def __init__(self, x, y, text, window):
        # Init
        self.x = x
        self.y = y
        self.text = text
        self.window = window

        # Personalized
        self.ID = 'Sign'
        self.textActive = False

        # Collider Values | Must set offsets and width/height
        self.width = 32
        self.height = 40
        self.xOffset = 16
        self.yOffset = 44

        self.collider = pygame.Rect(self.x + self.xOffset, self.y + self.yOffset, self.width, self.height)
    
    def tick(self, ticks):
        pass

    def render(self, scrollX, scrollY):
        pass
        # Render Sign Collider
        #self.window.drawRect(self.collider.x - scrollX, self.collider.y - scrollY, self.width, self.height, 255, 0, 0)