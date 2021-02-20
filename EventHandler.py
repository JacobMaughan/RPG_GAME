# Description: Handles pygame events
# Author: Jacob Maughan

# Sys Imports
from Enums import GameState
from Enums import Direction
from Enums import PlayerState

# Lib Imports
import pygame

class EventHandler():
    def __init__(self, game, objectHandler):
        # Init
        self.game = game
        self.objectHandler = objectHandler

        # Setup state from event handler
        self.eventState = None

        # Setup game state variables
        self.player = None

    def tick(self, ticks):
        # Check for pygame event
        for event in pygame.event.get():
            # Check close window event
            if event.type == pygame.QUIT:
                self.game.stop()

            # Check for game state change and set player insance if 
            if not self.eventState == self.game.state:
                self.eventState = self.game.state
                # If game state set player instance as player object
                if self.eventState == GameState.GAME:
                    self.player = self.objectHandler.getObjectByID('Player')

            if self.eventState == GameState.GAME:
                # check for key down
                if event.type == pygame.KEYDOWN:
                    # Move up
                    if event.key == pygame.K_w:
                        self.player.move(True, 0, -1)
                    # Move left
                    if event.key == pygame.K_a:
                        self.player.move(True, -1, 0)
                    # Move down
                    if event.key == pygame.K_s:
                        self.player.move(True, 0, 1)
                    # Move right
                    if event.key == pygame.K_d:
                        self.player.move(True, 1, 0)
                    # Attack
                    if event.key == pygame.K_r:
                        self.player.attack(self.objectHandler)
                    
                    # Added for development purposes | Must remove
                    if event.key == pygame.K_LSHIFT:
                        self.player.speed = 4
                    if event.key == pygame.K_LEFT:
                        self.objectHandler.scrollX -= 1
                    if event.key == pygame.K_RIGHT:
                        self.objectHandler.scrollX += 1
                    if event.key == pygame.K_UP:
                        self.objectHandler.scrollY -= 1
                    if event.key == pygame.K_DOWN:
                        self.objectHandler.scrollY += 1
                    if event.key == pygame.K_m:
                        self.player.saveSettings()
                        print('Settings saved!')

                # Check for key up
                if event.type == pygame.KEYUP:
                    # Check for vertical movement and set direction if needed
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        self.player.move(False, 0, 1)
                    
                    # Check for horizontal movement
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        self.player.move(False, 1, 0)
                    
                    # Added for development purposes | Must remove
                    if event.key == pygame.K_LSHIFT:
                        self.player.speed = 1
                    