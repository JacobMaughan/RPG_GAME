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

        # Setup player instance
        self.player = None

    def tick(self, ticks):
        # Check for pygame event
        for event in pygame.event.get():
            # Check close window event
            if event.type == pygame.QUIT:
                self.game.stop()

            # Check for game state change and update state for event handler
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
                        self.player.velY = -1
                        # Set state and direction if needed
                        self.player.playerState = PlayerState.WALKING
                        if self.player.velX == -1: self.player.direction = Direction.LEFT_UP
                        elif self.player.velX == 1: self.player.direction = Direction.RIGHT_UP
                        else: self.player.direction = Direction.UP
                    # Move left
                    if event.key == pygame.K_a:
                        self.player.velX = -1
                        # Set state and direction if needed
                        self.player.playerState = PlayerState.WALKING
                        if self.player.velY == -1: self.player.direction = Direction.LEFT_UP
                        elif self.player.velY == 1: self.player.direction = Direction.LEFT_DOWN
                        else: self.player.direction = Direction.LEFT
                    # Move down
                    if event.key == pygame.K_s:
                        self.player.velY = 1
                        # Set state and direction if needed
                        self.player.playerState = PlayerState.WALKING
                        if self.player.velX == -1: self.player.direction = Direction.LEFT_DOWN
                        elif self.player.velX == 1: self.player.direction = Direction.RIGHT_DOWN
                        else: self.player.direction = Direction.DOWN
                    # Move right
                    if event.key == pygame.K_d:
                        self.player.velX = 1
                        # Set state and direction if needed
                        self.player.playerState = PlayerState.WALKING
                        if self.player.velY == -1: self.player.direction = Direction.RIGHT_UP
                        elif self.player.velY == 1: self.player.direction = Direction.RIGHT_DOWN
                        else: self.player.direction = Direction.RIGHT

                # Check for key up
                if event.type == pygame.KEYUP:
                    # Check for vertical movement
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        self.player.velY = 0
                        # Set direction if needed
                        if self.player.velX == -1: self.player.direction = Direction.LEFT
                        elif self.player.velX == 1: self.player.direction = Direction.RIGHT
                    # Check for horizontal movement
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        self.player.velX = 0
                        # Set direction if needed
                        if self.player.velY == -1: self.player.direction = Direction.UP
                        elif self.player.velY == 1: self.player.direction = Direction.DOWN
                    