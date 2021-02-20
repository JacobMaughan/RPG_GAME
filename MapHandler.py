# Description: Handles generating maps
# Author: Jacob Maughan

# Lib Imports
import pygame

# Local Imports
from Enums import Direction
from JsonHandler import JsonHandler
from SpriteSheet import SpriteSheet
from SignTrigger import SignTrigger
from ZoneTrigger import ZoneTrigger
from Tile import Tile

class MapHandler():
    def __init__(self, scaleFactor, objectHandler, window):
        # Init
        self.scaleFactor = scaleFactor
        self.objectHandler = objectHandler
        self.window = window

        self.mapsFile = JsonHandler('./assets/data/maps.json')
        self.mapsData = self.mapsFile.getJson()

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
    
    # Load selected map | Must be equal propotions for scroll clamp to work
    def loadMap(self, mapFile):
        mapToLoad = self.mapsData[mapFile]
        map = mapToLoad['map']
        signData = mapToLoad['signs']
        newZoneData = mapToLoad['newZoneTriggers']
        self.objectHandler.setScrollClamp(len(map[0]) * self.tileSize, len(map) * self.tileSize)
        for y in range(len(map)):
            for x in range(len(map[y])):
                # Grass
                    if map[y][x] == 'S':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                    # Bushes Top
                    elif map[y][x] == 'W':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[19][5], True, self.window))
                    # Bushes Left
                    elif map[y][x] == 'A':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[18][7], True, self.window))
                    # Bushes Bottom
                    elif map[y][x] == 'X':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[18][5], True, self.window))
                    # Bushes Right
                    elif map[y][x] == 'D':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[18][6], True, self.window))
                    # Bushes Left Top
                    elif map[y][x] == 'Q':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[19][4], True, self.window))
                    # Bushes Left Bottom
                    elif map[y][x] == 'Z':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[16][4], True, self.window))
                    # Bushes Right Bottom
                    elif map[y][x] == 'C':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[16][3], True, self.window))
                    # Bushes Right Top
                    elif map[y][x] == 'E':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[19][3], True, self.window))
                    # Bushes Closed Left Top
                    elif map[y][x] == 'U':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[16][5], True, self.window))
                    # Bushes Closed Left Bottom
                    elif map[y][x] == 'J':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[17][5], True, self.window))
                    # Bushes Closed Right Bottom
                    elif map[y][x] == 'K':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[17][6], True, self.window))
                    # Bushed Closed Right Top
                    elif map[y][x] == 'I':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[16][6], True, self.window))
                    # Road
                    elif map[y][x] == 'G':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[30][1], False, self.window))
                    # Road Top
                    elif map[y][x] == 'T':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[29][1], False, self.window))
                    # Road Left
                    elif map[y][x] == 'F':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[30][0], False, self.window))
                    # Road Bottom    
                    elif map[y][x] == 'B':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[31][1], False, self.window))
                    # Road Right  
                    elif map[y][x] == 'H':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[30][2], False, self.window))
                    # Road Left Top
                    elif map[y][x] == 'R':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[29][0], False, self.window))
                    # Road Left Bottom   
                    elif map[y][x] == 'V':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[31][0], False, self.window))
                    # Road Right Bottom
                    elif map[y][x] == 'N':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[31][2], False, self.window))
                    # Road Right Top
                    elif map[y][x] == 'Y':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[29][2], False, self.window))
                    # Road Corner Left Top
                    elif map[y][x] == 'O':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[32][0], False, self.window))
                    # Road Corner Left Bottom
                    elif map[y][x] == 'L':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[33][0], False, self.window))
                    # Road Corner Right Bottom
                    elif map[y][x] == ':':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[33][1], False, self.window))
                    # Road Corner Right Top
                    elif map[y][x] == 'P':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[32][1], False, self.window))
                    # Sign
                    elif map[y][x] == '1':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._sprites[2][35], True, self.window))
        for i in range(len(signData)):
            self.objectHandler.addObject(SignTrigger(signData[i]['x'], signData[i]['y'], signData[i]['text'], self.window))
        for i in range(len(newZoneData)):
            self.objectHandler.addObject(ZoneTrigger(newZoneData[i]['x'], newZoneData[i]['y'], newZoneData[i]['size'], Direction(newZoneData[i]['direction']), newZoneData[i]['newZone'], newZoneData[i]['newX'], newZoneData[i]['newY'], self.scaleFactor, self, self.objectHandler, self.window))