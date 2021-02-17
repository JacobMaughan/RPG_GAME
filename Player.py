# Description: The player object
# Author: Jacob Maughan

# Lib Imports
import pygame

# Local Imports
from Enums import Direction
from Enums import PlayerState
from SpriteSheet import SpriteSheet

class Player():
    def __init__(self, x, y, width, height, window):
        # Init
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window

        # Personalized
        self.ID = 'Player'
        self.velX = 0
        self.velY = 0
        self.lastVelX = 0
        self.lastVelY = 0
        self.speed = 1

        # State
        self.playerState = PlayerState.IDLE
        self.direction = Direction.DOWN

        # Idle Sprites
        self.spriteSheet = SpriteSheet('./assets/character.png')
        self.lookUpSprite = self.spriteSheet.getImage(0, 64, 16, 32)
        self.lookUpSprite = pygame.transform.scale(self.lookUpSprite, (self.width, self.height))
        self.lookLeftSprite = self.spriteSheet.getImage(0, 96, 16, 32)
        self.lookLeftSprite = pygame.transform.scale(self.lookLeftSprite, (self.width, self.height))
        self.lookDownSprite = self.spriteSheet.getImage(0, 0, 16, 32)
        self.lookDownSprite = pygame.transform.scale(self.lookDownSprite, (self.width, self.height))
        self.lookRightSprite = self.spriteSheet.getImage(0, 32, 16, 32)
        self.lookRightSprite = pygame.transform.scale(self.lookRightSprite, (self.width, self.height))

        # Walk Up Sprites
        self.walkUpSpriteOne = self.spriteSheet.getImage(16, 64, 16, 32)
        self.walkUpSpriteOne = pygame.transform.scale(self.walkUpSpriteOne, (self.width, self.height))
        self.walkUpSpriteTwo = self.spriteSheet.getImage(32, 64, 16, 32)
        self.walkUpSpriteTwo = pygame.transform.scale(self.walkUpSpriteTwo, (self.width, self.height))
        self.walkUpSpriteThree = self.spriteSheet.getImage(48, 64, 16, 32)
        self.walkUpSpriteThree = pygame.transform.scale(self.walkUpSpriteThree, (self.width, self.height))

        # Walk Left Sprites
        self.walkLeftSpriteOne = self.spriteSheet.getImage(16, 96, 16, 32)
        self.walkLeftSpriteOne = pygame.transform.scale(self.walkLeftSpriteOne, (self.width, self.height))
        self.walkLeftSpriteTwo = self.spriteSheet.getImage(32, 96, 16, 32)
        self.walkLeftSpriteTwo = pygame.transform.scale(self.walkLeftSpriteTwo, (self.width, self.height))
        self.walkLeftSpriteThree = self.spriteSheet.getImage(48, 96, 16, 32)
        self.walkLeftSpriteThree = pygame.transform.scale(self.walkLeftSpriteThree, (self.width, self.height))

        # Walk Down Sprites
        self.walkDownSpriteOne = self.spriteSheet.getImage(16, 0, 16, 32)
        self.walkDownSpriteOne = pygame.transform.scale(self.walkDownSpriteOne, (self.width, self.height))
        self.walkDownSpriteTwo = self.spriteSheet.getImage(32, 0, 16, 32)
        self.walkDownSpriteTwo = pygame.transform.scale(self.walkDownSpriteTwo, (self.width, self.height))
        self.walkDownSpriteThree = self.spriteSheet.getImage(48, 0, 16, 32)
        self.walkDownSpriteThree = pygame.transform.scale(self.walkDownSpriteThree, (self.width, self.height))

        # Walk Right Sprites
        self.walkRightSpriteOne = self.spriteSheet.getImage(16, 32, 16, 32)
        self.walkRightSpriteOne = pygame.transform.scale(self.walkRightSpriteOne, (self.width, self.height))
        self.walkRightSpriteTwo = self.spriteSheet.getImage(32, 32, 16, 32)
        self.walkRightSpriteTwo = pygame.transform.scale(self.walkRightSpriteTwo, (self.width, self.height))
        self.walkRightSpriteThree = self.spriteSheet.getImage(48, 32, 16, 32)
        self.walkRightSpriteThree = pygame.transform.scale(self.walkRightSpriteThree, (self.width, self.height))

        # Active Walking Sprite
        self.activeWalkingSprite = None

        # Collision
        self.collider = pygame.Rect(self.x, self.y, self.width, self.height)

    def tick(self, ticks):
        # Move player by vel
        self.x += self.velX * self.speed
        self.y += self.velY * self.speed

        # Set collider to x and y value
        self.collider.x = self.x
        self.collider.y = self.y

        # Set player state if stopped walking
        if self.playerState == PlayerState.WALKING:
            if self.velX == 0 and self.velY == 0:
                self.playerState = PlayerState.IDLE

        # Set Walking Animation Frame For Sprite
        if self.playerState == PlayerState.WALKING:
            if ticks in range(20):
                if self.direction == Direction.UP: self.activeWalkingSprite = self.lookUpSprite
                elif self.direction == Direction.LEFT: self.activeWalkingSprite = self.lookLeftSprite
                elif self.direction == Direction.DOWN: self.activeWalkingSprite = self.lookDownSprite
                elif self.direction == Direction.RIGHT: self.activeWalkingSprite = self.lookRightSprite
                elif self.direction == Direction.LEFT_UP: self.activeWalkingSprite = self.lookLeftSprite
                elif self.direction == Direction.LEFT_DOWN: self.activeWalkingSprite = self.lookLeftSprite
                elif self.direction == Direction.RIGHT_UP: self.activeWalkingSprite = self.lookRightSprite
                elif self.direction == Direction.RIGHT_DOWN: self.activeWalkingSprite = self.lookRightSprite
            elif ticks in range(20, 40):
                if self.direction == Direction.UP: self.activeWalkingSprite = self.walkUpSpriteOne
                elif self.direction == Direction.LEFT: self.activeWalkingSprite = self.walkLeftSpriteOne
                elif self.direction == Direction.DOWN: self.activeWalkingSprite = self.walkDownSpriteOne
                elif self.direction == Direction.RIGHT: self.activeWalkingSprite = self.walkRightSpriteOne
                elif self.direction == Direction.LEFT_UP: self.activeWalkingSprite = self.walkLeftSpriteOne
                elif self.direction == Direction.LEFT_DOWN: self.activeWalkingSprite = self.walkLeftSpriteOne
                elif self.direction == Direction.RIGHT_UP: self.activeWalkingSprite = self.walkRightSpriteOne
                elif self.direction == Direction.RIGHT_DOWN: self.activeWalkingSprite = self.walkRightSpriteOne
            elif ticks in range(40, 60):
                if self.direction == Direction.UP: self.activeWalkingSprite = self.walkUpSpriteTwo
                elif self.direction == Direction.LEFT: self.activeWalkingSprite = self.walkLeftSpriteTwo
                elif self.direction == Direction.DOWN: self.activeWalkingSprite = self.walkDownSpriteTwo
                elif self.direction == Direction.RIGHT: self.activeWalkingSprite = self.walkRightSpriteTwo
                elif self.direction == Direction.LEFT_UP: self.activeWalkingSprite = self.walkLeftSpriteTwo
                elif self.direction == Direction.LEFT_DOWN: self.activeWalkingSprite = self.walkLeftSpriteTwo
                elif self.direction == Direction.RIGHT_UP: self.activeWalkingSprite = self.walkRightSpriteTwo
                elif self.direction == Direction.RIGHT_DOWN: self.activeWalkingSprite = self.walkRightSpriteTwo
            elif ticks in range(60, 80):
                if self.direction == Direction.UP: self.activeWalkingSprite = self.walkUpSpriteThree
                elif self.direction == Direction.LEFT: self.activeWalkingSprite = self.walkLeftSpriteThree
                elif self.direction == Direction.DOWN: self.activeWalkingSprite = self.walkDownSpriteThree
                elif self.direction == Direction.RIGHT: self.activeWalkingSprite = self.walkRightSpriteThree
                elif self.direction == Direction.LEFT_UP: self.activeWalkingSprite = self.walkLeftSpriteThree
                elif self.direction == Direction.LEFT_DOWN: self.activeWalkingSprite = self.walkLeftSpriteThree
                elif self.direction == Direction.RIGHT_UP: self.activeWalkingSprite = self.walkRightSpriteThree
                elif self.direction == Direction.RIGHT_DOWN: self.activeWalkingSprite = self.walkRightSpriteThree
            elif ticks in range(80, 100):
                if self.direction == Direction.UP: self.activeWalkingSprite = self.lookUpSprite
                elif self.direction == Direction.LEFT: self.activeWalkingSprite = self.lookLeftSprite
                elif self.direction == Direction.DOWN: self.activeWalkingSprite = self.lookDownSprite
                elif self.direction == Direction.RIGHT: self.activeWalkingSprite = self.lookRightSprite
                elif self.direction == Direction.LEFT_UP: self.activeWalkingSprite = self.lookLeftSprite
                elif self.direction == Direction.LEFT_DOWN: self.activeWalkingSprite = self.lookLeftSprite
                elif self.direction == Direction.RIGHT_UP: self.activeWalkingSprite = self.lookRightSprite
                elif self.direction == Direction.RIGHT_DOWN: self.activeWalkingSprite = self.lookRightSprite
            elif ticks >= 100:
                if self.direction == Direction.UP: self.activeWalkingSprite = self.walkUpSpriteOne
                elif self.direction == Direction.LEFT: self.activeWalkingSprite = self.walkLeftSpriteOne
                elif self.direction == Direction.DOWN: self.activeWalkingSprite = self.walkDownSpriteOne
                elif self.direction == Direction.RIGHT: self.activeWalkingSprite = self.walkRightSpriteOne
                elif self.direction == Direction.LEFT_UP: self.activeWalkingSprite = self.walkLeftSpriteOne
                elif self.direction == Direction.LEFT_DOWN: self.activeWalkingSprite = self.walkLeftSpriteOne
                elif self.direction == Direction.RIGHT_UP: self.activeWalkingSprite = self.walkRightSpriteOne
                elif self.direction == Direction.RIGHT_DOWN: self.activeWalkingSprite = self.walkRightSpriteOne

    def render(self, scrollX, scrollY):
        # Render Sprite
        if self.playerState == PlayerState.IDLE:
            if self.direction == Direction.UP:
                self.window.drawSprite(self.x - scrollX, self.y - scrollY, self.width, self.height, self.lookUpSprite)
            elif self.direction == Direction.LEFT:
                self.window.drawSprite(self.x - scrollX, self.y - scrollY, self.width, self.height, self.lookLeftSprite)
            elif self.direction == Direction.DOWN:
                self.window.drawSprite(self.x - scrollX, self.y - scrollY, self.width, self.height, self.lookDownSprite)
            elif self.direction == Direction.RIGHT:
                self.window.drawSprite(self.x - scrollX, self.y - scrollY, self.width, self.height, self.lookRightSprite)
        elif self.playerState == PlayerState.WALKING:
            self.window.drawSprite(self.x - scrollX, self.y - scrollY, self.width, self.height, self.activeWalkingSprite)
    
    def collide(self, object):
        print('Collision:' + object.ID)