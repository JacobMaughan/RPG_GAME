# Description: The zone trigger object
# Author: Jacob Maughan

# Lib Imports
import pygame

# Local Imports
from Enums import Direction

class ZoneTrigger():
    def __init__(self, x, y, size, direction, newZone, newX, newY, mapHandler, objectHandler, window):
        # Init
        self.x = x
        self.y = y
        self.direction = direction
        self.newZone = newZone
        self.newX = newX
        self.newY = newY
        self.objectHandler = objectHandler
        self.mapHandler = mapHandler
        self.window = window

        self.size = size * 16 * self.window.scaleFactor

        # Personalized
        self.ID = 'NewZoneTrigger'

        # Collider Values | Must set offsets and width/height
        if self.direction == Direction.UP:
            self.width = self.size
            self.height = 10
            self.yOffset = -10
            self.xOffset = 0
        elif self.direction == Direction.LEFT:
            self.width = 10
            self.height = self.size
            self.yOffset = 0
            self.xOffset = -10
        elif self.direction == Direction.DOWN:
            self.width = self.size
            self.height = 10
            self.yOffset = 64
            self.xOffset = 0
        elif self.direction == Direction.RIGHT:
            self.width = 10
            self.height = self.size
            self.yOffset = 0
            self.xOffset = 64

        self.collider = pygame.Rect(self.x + self.xOffset, self.y + self.yOffset, self.width, self.height)
    
    def tick(self, ticks):
        pass

    def render(self, scrollX, scrollY):
        pass
        # Render Trigger Collider
        #self.window.drawRect(self.collider.x - scrollX, self.collider.y - scrollY, self.width, self.height, 255, 0, 0)
    
    def loadNewZone(self):
        player = self.objectHandler.getObjectByID('Player')
        ui = self.objectHandler.getObjectByID('UI')
        player.map = self.newZone
        player.x = self.newX
        player.y = self.newY
        self.objectHandler.clearObjects()
        self.mapHandler.loadMap(self.newZone)
        self.objectHandler.addObject(player)
        self.objectHandler.addObject(ui)
        if self.direction == Direction.UP:
            self.objectHandler.scrollY = self.objectHandler.scrollClampY
        elif self.direction == Direction.LEFT:
            self.objectHandler.scrollX = self.objectHandler.scrollClampX
        elif self.direction == Direction.DOWN:
            self.objectHandler.scrollY = 0
        elif self.direction == Direction.RIGHT:
            self.objectHandler.scrollX = 0