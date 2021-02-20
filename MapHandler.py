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
from Enemy import Enemy
from Tile import Tile

class MapHandler():
    def __init__(self, objectHandler, window):
        # Init
        self.objectHandler = objectHandler
        self.window = window

        self.mapsFile = JsonHandler('./assets/data/maps.json')
        self.mapsData = self.mapsFile.getJson()

        self.tileSize = 16 * self.window.scaleFactor

        # Creating spritesheet
        self.tileSpriteSheet = SpriteSheet('./assets/art/overworld.png')
        self.objectSpriteSheet = SpriteSheet('./assets/art/objects.png')

        # Get sprite array's
        # Tile X - 40
        # Tile Y - 36
        self._tileSprites = self.tileSpriteSheet.getImageArray(16, 16, self.tileSize, self.tileSize)
        self._objectSprites = self.objectSpriteSheet.getImageArray(16, 16, self.tileSize, self.tileSize)
    
    # Load selected map | Must be equal propotions for scroll clamp to work
    def loadMap(self, mapFile):
        mapToLoad = self.mapsData[mapFile]
        map = mapToLoad['map']
        signData = mapToLoad['signs']
        newZoneData = mapToLoad['newZoneTriggers']
        enemyData = mapToLoad['enemys']
        self.objectHandler.setScrollClamp(len(map[0]) * self.tileSize, len(map) * self.tileSize)
        for y in range(len(map)):
            for x in range(len(map[y])):
                # Grass
                    if map[y][x] == 'S':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[0][0], False, self.window))
                    # Bushes Top
                    elif map[y][x] == 'W':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[19][5], True, self.window))
                    # Bushes Left
                    elif map[y][x] == 'A':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[18][7], True, self.window))
                    # Bushes Bottom
                    elif map[y][x] == 'X':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[18][5], True, self.window))
                    # Bushes Right
                    elif map[y][x] == 'D':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[18][6], True, self.window))
                    # Bushes Left Top
                    elif map[y][x] == 'Q':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[19][4], True, self.window))
                    # Bushes Left Bottom
                    elif map[y][x] == 'Z':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[16][4], True, self.window))
                    # Bushes Right Bottom
                    elif map[y][x] == 'C':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[16][3], True, self.window))
                    # Bushes Right Top
                    elif map[y][x] == 'E':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[19][3], True, self.window))
                    # Bushes Closed Left Top
                    elif map[y][x] == 'U':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[16][5], True, self.window))
                    # Bushes Closed Left Bottom
                    elif map[y][x] == 'J':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[17][5], True, self.window))
                    # Bushes Closed Right Bottom
                    elif map[y][x] == 'K':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[17][6], True, self.window))
                    # Bushed Closed Right Top
                    elif map[y][x] == 'I':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[16][6], True, self.window))
                    # Road
                    elif map[y][x] == 'G':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[30][1], False, self.window))
                    # Road Top
                    elif map[y][x] == 'T':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[29][1], False, self.window))
                    # Road Left
                    elif map[y][x] == 'F':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[30][0], False, self.window))
                    # Road Bottom    
                    elif map[y][x] == 'B':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[31][1], False, self.window))
                    # Road Right  
                    elif map[y][x] == 'H':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[30][2], False, self.window))
                    # Road Left Top
                    elif map[y][x] == 'R':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[29][0], False, self.window))
                    # Road Left Bottom   
                    elif map[y][x] == 'V':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[31][0], False, self.window))
                    # Road Right Bottom
                    elif map[y][x] == 'N':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[31][2], False, self.window))
                    # Road Right Top
                    elif map[y][x] == 'Y':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[29][2], False, self.window))
                    # Road Corner Left Top
                    elif map[y][x] == 'O':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[32][0], False, self.window))
                    # Road Corner Left Bottom
                    elif map[y][x] == 'L':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[33][0], False, self.window))
                    # Road Corner Right Bottom
                    elif map[y][x] == ':':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[33][1], False, self.window))
                    # Road Corner Right Top
                    elif map[y][x] == 'P':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[32][1], False, self.window))
                    # Sign
                    elif map[y][x] == '1':
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[0][0], False, self.window))
                        self.objectHandler.addObject(Tile(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize, self._tileSprites[2][35], True, self.window))
        for i in range(len(signData)):
            self.objectHandler.addObject(SignTrigger(signData[i]['x'], signData[i]['y'], signData[i]['text'], signData[i]['size'], [self._objectSprites[15][10], self._objectSprites[14][10], self._objectSprites[14][9], self._objectSprites[15][9], self._objectSprites[16][9], self._objectSprites[16][10], self._objectSprites[16][11], self._objectSprites[15][11], self._objectSprites[14][11]], self.window))
        for i in range(len(newZoneData)):
            self.objectHandler.addObject(ZoneTrigger(newZoneData[i]['x'], newZoneData[i]['y'], newZoneData[i]['size'], Direction(newZoneData[i]['direction']), newZoneData[i]['newZone'], newZoneData[i]['newX'], newZoneData[i]['newY'], self, self.objectHandler, self.window))
        for i in range(len(enemyData)):
            self.objectHandler.addObject(Enemy(enemyData[i]['x'], enemyData[i]['y'], Direction(enemyData[i]['direction']), self.objectHandler, self.window))