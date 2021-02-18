# Description: Handles generating maps
# Author: Jacob Maughan

# Lib Imports
import pygame

# Local Imports
from SpriteSheet import SpriteSheet
from Tile import Tile

class MapHandler():
    def __init__(self, scaleFactor, objectHandler, window):
        # Init
        self.objectHandler = objectHandler
        self.window = window

        # Setting tiles width and height
        self.tileWidth = 16 * scaleFactor
        self.tileHeight = 16 * scaleFactor

        # Creating spritesheet
        self.spriteSheet = SpriteSheet('./assets/art/overworld.png')

        # Load Sprites into array
        self._sprites = [[]]
        spriteY = 0
        y = 0
        while spriteY < 576:
            spriteX = 0
            x = 0
            while x < 640:
                self._sprites[y].append(self.spriteSheet.getImage(spriteX, spriteY ,16, 16))
                self._sprites[y][x] = pygame.transform.scale(self._sprites[y][x], (self.tileWidth, self.tileHeight))
                spriteX += 16
                x += 1
            self._sprites.append([])
            spriteY += 16
            y += 1
    
    # Load selected map
    def loadMap(self, mapFile):
        with open('./assets/maps/' + mapFile + '.mp', 'r') as file:
            y = 0
            for line in file:
                for x in range(len(line)):
                    # Grass
                    if line[x] == '0':
                        self.objectHandler.addObject(Tile(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight, self._sprites[0][0], False, self.window))
                    # Bushes Facing Bottom
                    elif line[x] == '1':
                        self.objectHandler.addObject(Tile(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight, self._sprites[19][5], True, self.window))
                    # Bushes Facing Right
                    elif line[x] == '2':
                        self.objectHandler.addObject(Tile(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight, self._sprites[18][7], True, self.window))
                    # Bushes Facing Top
                    elif line[x] == '3':
                        self.objectHandler.addObject(Tile(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight, self._sprites[18][5], True, self.window))
                    # Bushes Facing Left
                    elif line[x] == '4':
                        self.objectHandler.addObject(Tile(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight, self._sprites[18][6], True, self.window))
                    # Bushes Facing Bottom Right
                    elif line[x] == '5':
                        self.objectHandler.addObject(Tile(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight, self._sprites[19][4], True, self.window))
                    # Bushes Facing Top Right
                    elif line[x] == '6':
                        self.objectHandler.addObject(Tile(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight, self._sprites[16][4], True, self.window))
                    # Bushes Facing Top Left
                    elif line[x] == '7':
                        self.objectHandler.addObject(Tile(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight, self._sprites[16][3], True, self.window))
                    # Bushes Facing Bottom Left
                    elif line[x] == '8':
                        self.objectHandler.addObject(Tile(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileWidth, y * self.tileHeight, self.tileWidth, self.tileHeight, self._sprites[19][3], True, self.window))
                y += 1