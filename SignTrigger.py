# Description: The sign trigger object
# Author: Jacob Maughan

# Lib Imports
import pygame

class SignTrigger():
    def __init__(self, x, y, text, size, sprites, window):
        # Init
        self.x = x
        self.y = y
        self.text = text
        self.size = size
        self.sprites = sprites
        self.window = window

        self.font = pygame.font.SysFont('Arial Black', self.size)

        # Rescaling Sprites
        self.sprites[0] = pygame.transform.scale(self.sprites[0], (self.window.screen.get_width() - 16 * 4 * self.window.scaleFactor, 16 * 2 * self.window.scaleFactor))
        self.sprites[1] = pygame.transform.scale(self.sprites[1], (self.window.screen.get_width() - 16 * 4 * self.window.scaleFactor, self.sprites[1].get_height()))
        self.sprites[3] = pygame.transform.scale(self.sprites[3], (self.sprites[3].get_width(), 16 * 2 * self.window.scaleFactor))
        self.sprites[5] = pygame.transform.scale(self.sprites[5], (self.window.screen.get_width() - 16 * 4 * self.window.scaleFactor, self.sprites[1].get_height()))
        self.sprites[7] = pygame.transform.scale(self.sprites[7], (self.sprites[3].get_width(), 16 * 2 * self.window.scaleFactor))

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
        if self.textActive:
            self.window.drawSprite(16 * 2 * self.window.scaleFactor, self.window.screen.get_height() - 16 * 4 * self.window.scaleFactor, self.sprites[0])
            self.window.drawSprite(16 * 2 * self.window.scaleFactor, self.window.screen.get_height() - 16 * 5 * self.window.scaleFactor, self.sprites[1])
            self.window.drawSprite(16 * self.window.scaleFactor, self.window.screen.get_height() - 16 * 5 * self.window.scaleFactor, self.sprites[2])
            self.window.drawSprite(16 * self.window.scaleFactor, self.window.screen.get_height() - 16 * 4 * self.window.scaleFactor, self.sprites[3])
            self.window.drawSprite(16 * self.window.scaleFactor, self.window.screen.get_height() - 16 * 2 * self.window.scaleFactor, self.sprites[4])
            self.window.drawSprite(16 * 2 * self.window.scaleFactor, self.window.screen.get_height() - 16 * 2 * self.window.scaleFactor, self.sprites[5])
            self.window.drawSprite(self.window.screen.get_width() - 16 * 2 * self.window.scaleFactor, self.window.screen.get_height() - 16 * 2 * self.window.scaleFactor, self.sprites[6])
            self.window.drawSprite(self.window.screen.get_width() - 16 * 2 * self.window.scaleFactor, self.window.screen.get_height() - 16 * 4 * self.window.scaleFactor, self.sprites[7])
            self.window.drawSprite(self.window.screen.get_width() - 16 * 2 * self.window.scaleFactor, self.window.screen.get_height() - 16 * 5 * self.window.scaleFactor, self.sprites[8])
            self.window.drawText(16 * 2 * self.window.scaleFactor, self.window.screen.get_height() - 16 * 4 * self.window.scaleFactor, self.text, self.font)
            