# Description: The main game file
# Author: Jacob Maughan

# Sys Imports
import time

# Lib Imports
import pygame

# Local Imports
from Enums import Direction
from Enums import GameState
from Window import Window
from JsonHandler import JsonHandler
from EventHandler import EventHandler
from ObjectHandler import ObjectHandler
from MapHandler import MapHandler
from MainMenu import MainMenu
from Player import Player
from UI import UI

class Game():
    def __init__(self):
        # Initilize pygame
        pygame.init()

        # Load settings
        self.settingsFile = JsonHandler('./assets/data/settings.json')
        self.settingsData = self.settingsFile.getJson()
        self.playerFile = JsonHandler('./assets/data/player.json')
        self.playerData = self.playerFile.getJson()

        # Set width and height from settings
        self.width = self.settingsData['width']
        self.height = self.settingsData['height']

        # Sprite scale from settings
        self.scaleFactor = self.settingsData['scaleFactor']

        # Create instance of window and handlers
        self.window = Window(self.scaleFactor, self.width, self.height, 'RPG_GAME', 'assets/art/logo.png')
        self.objectHandler = ObjectHandler(self)
        self.eventHandler = EventHandler(self, self.objectHandler)
        self.mapHandler = MapHandler(self.objectHandler, self.window)

        # Setup game state
        self.state = None
        self.lastState = None

        # Game speed/Tick speed setup
        self.tickSpeed = 120
        self.ticks = 0

    def tick(self):
        # Setup tick counter | If tick count hit tickSpeed,  1 second has elapsed and set ticks to 0
        self.ticks += 1
        
        # Check if state has changed and load objects if has
        if not self.lastState == self.state:
            self.lastState = self.state
            self.loadObjects()

        # Tick handlers with tick counter as arg
        self.eventHandler.tick(self.ticks)
        self.objectHandler.tick(self.ticks)

    def render(self):
        # Render background
        self.window.fillScreen(0, 0, 0)

        # Render objects
        self.objectHandler.render()

        # Update pygame display
        pygame.display.update()

    def loadObjects(self):
        # Check gamestate and load correct objects
        if self.state == GameState.MAIN_MENU:
            self.objectHandler.clearObjects()
            self.objectHandler.addObject(MainMenu(self, self.window))
        elif self.state == GameState.GAME:
            self.objectHandler.clearObjects()
            self.mapHandler.loadMap(self.playerData['map'])
            self.objectHandler.addObject(Player(self.playerFile, self.window))
            print(self.objectHandler.getObjectByID('Player'))
            self.objectHandler.addObject(UI(self.objectHandler, self.window))
        elif self.state == GameState.PAUSE:
            pass

    def run(self):
        # Setup delta time to tick specific amount per second
        lastTime = time.time()
        dt = 0
        while self._running:
            # Update delta time
            dt += (time.time() - lastTime) * self.tickSpeed
            lastTime = time.time()
            if(dt >= 1):
                # Tick if enough time passed
                self.tick()
                dt -= 1
            # Render always
            self.render()
        
    def start(self):
        # Init game
        self._running = True
        self.state = GameState.MAIN_MENU
        self.run()
    
    def stop(self):
        # Stop game
        self._running = False

# Setup main game instance
game = Game()
game.start()