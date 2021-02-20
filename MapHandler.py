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

        self.tileSize = 16 * scaleFactor

        # Creating spritesheet
        self.spriteSheet = SpriteSheet('./assets/art/overworld.png')

        # Load Sprites into array
        # X - 40
        # Y - 36
        self._sprites = [[]]
        spriteY = 0
        y = 0
        while spriteY < 576:
            spriteX = 0
            x = 0
            while x < 640:
                self._sprites[y].append(self.spriteSheet.getImage(spriteX, spriteY, 16, 16))
                self._sprites[y][x] = pygame.transform.scale(self._sprites[y][x], (self.tileSize, self.tileSize))
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
                    if line[x] == 'S':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                    # Bushes Top
                    elif line[x] == 'W':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[19][5], True, self.window))
                    # Bushes Left
                    elif line[x] == 'A':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[18][7], True, self.window))
                    # Bushes Bottom
                    elif line[x] == 'X':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[18][5], True, self.window))
                    # Bushes Right
                    elif line[x] == 'D':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[18][6], True, self.window))
                    # Bushes Left Top
                    elif line[x] == 'Q':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[19][4], True, self.window))
                    # Bushes Left Bottom
                    elif line[x] == 'Z':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[16][4], True, self.window))
                    # Bushes Right Bottom
                    elif line[x] == 'C':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[16][3], True, self.window))
                    # Bushes Right Top
                    elif line[x] == 'E':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[19][3], True, self.window))
                    # Bushes Closed Left Top
                    elif line[x] == 'U':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[16][5], True, self.window))
                    # Bushes Closed Left Bottom
                    elif line[x] == 'J':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[17][5], True, self.window))
                    # Bushes Closed Right Bottom
                    elif line[x] == 'K':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[17][6], True, self.window))
                    # Bushed Closed Right Top
                    elif line[x] == 'I':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[16][6], True, self.window))
                    # Road
                    elif line[x] == 'G':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[30][1], False, self.window))
                    # Road Top
                    elif line[x] == 'T':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[29][1], False, self.window))
                    # Road Left
                    elif line[x] == 'F':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[30][0], False, self.window))
                    # Road Bottom    
                    elif line[x] == 'B':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[31][1], False, self.window))
                    # Road Right  
                    elif line[x] == 'H':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[30][2], False, self.window))
                    # Road Left Top
                    elif line[x] == 'R':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[29][0], False, self.window))
                    # Road Left Bottom   
                    elif line[x] == 'V':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[31][0], False, self.window))
                    # Road Right Bottom
                    elif line[x] == 'N':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[31][2], False, self.window))
                    # Road Right Top
                    elif line[x] == 'Y':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[29][2], False, self.window))
                    # Road Corner Left Top
                    elif line[x] == 'O':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[32][0], False, self.window))
                    # Road Corner Left Bottom
                    elif line[x] == 'L':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[33][0], False, self.window))
                    # Road Corner Right Bottom
                    elif line[x] == ':':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[33][1], False, self.window))
                    # Road Corner Right Top
                    elif line[x] == 'P':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[32][1], False, self.window))
                y += 1
            # Set scroll clamp
            self.objectHandler.setScrollClamp(y * self.tileSize)