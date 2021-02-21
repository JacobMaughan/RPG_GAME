# Description: UI Object
# Author: Jacob Maughan

# Lib Imports
import pygame

class UI():
    def __init__(self, objectHandler, window):
        # Init
        self.objectHandler = objectHandler
        self.window = window

        # Personalized
        self.ID = 'UI'
        self.player = None

        # UI Elements
        self.health = 100

        # Collider | For Attack
        self.collider = pygame.Rect(0, 0, 0, 0)

    def tick(self, ticks):
        if self.player == None:
            self.player = self.objectHandler.getObjectByID('Player')

        self.maxHealth = self.player.maxHealth
        self.health = self.player.health
    
    def render(self, scrollX, scrollY):
        self.window.drawRect(20, 20, 258, 43, 0, 0, 0)
        self.window.drawRect(24, 24, (self.health / self.maxHealth) * 250, 35, 255, 0, 0)