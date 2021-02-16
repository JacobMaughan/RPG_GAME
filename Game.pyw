# Description: The main game file
# Author: Jacob Maughan

# Sys Imports
import time

# Lib Imports
import pygame

# Local Imports
from JsonHandler import JsonHandler
from Window import Window
from EventHandler import EventHandler
from ObjectHandler import ObjectHandler
from Player import Player
from Block import Block
from Enums import GameState

class Game():
    def __init__(self):
        # Initilize pygame
        pygame.init()

        # Load settings
        self.settingsFile = JsonHandler('./json/settings.json')
        self.settingsData = self.settingsFile.getJson()

        # Set width and height from settings
        self.width = self.settingsData['width']
        self.height = self.settingsData['height']

        # Create instance of window and handlers
        self.window = Window(self.width, self.height, 'RPG_GAME', 'path/to/logo.png')
        self.objectHandler = ObjectHandler(self)
        self.eventHandler = EventHandler(self, self.objectHandler)

        # Setup game state
        self.state = None
        self.lastState = None

        # Sprite scale
        self.scaleFactor = 4

        # Game speed/Tick speed setup
        self.tickSpeed = 120
        self.ticks = 0

    def tick(self):
        # Setup tick counter | If tick count hit tickSpeed,  1 second has elapsed and set ticks to 0
        self.ticks += 1
        if self.ticks == self.tickSpeed: self.ticks = 0

        # Tick handlers with tick counter as arg
        self.eventHandler.tick(self.ticks)
        self.objectHandler.tick(self.ticks)
        

    def render(self):
        # Render background
        self.window.fillScreen(0, 255, 0)

        # Render objects
        self.objectHandler.render()

        # Update pygame display
        pygame.display.update()

    def loadObjects(self):
        # Check gamestate and load correct objects
        if self.state == GameState.MAIN_MENU:
            self.objectHandler.clearObjects()
        elif self.state == GameState.GAME:
            self.objectHandler.clearObjects()
            self.objectHandler.addObject(Player(self.width / 2 - 16 * self.scaleFactor, self.height / 2 - 32 * self.scaleFactor, 16 * self.scaleFactor, 32 * self.scaleFactor, self.window))
            self.objectHandler.addObject(Block((self.width / 2 - 50), -75, 16 * self.scaleFactor, 16 * self.scaleFactor, self.window))
        elif self.state == GameState.PAUSE:
            pass

    def run(self):
        # Setup delta time to tick specific amount per second
        lastTime = time.time()
        dt = 0
        while self._running:
            # Check if state has changed and load objects if has
            if not self.lastState == self.state:
                self.lastState = self.state
                self.loadObjects()
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
        self.state = GameState.GAME
        self.run()
    
    def stop(self):
        # Stop game
        self._running = False

# Setup main game instance
game = Game()
game.start()