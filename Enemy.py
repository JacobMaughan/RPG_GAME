# Description: The enemy object
# Author: Jacob Maughan

# Sys Imports
import math

# Lib Imports
import pygame

# Local Imports
from Enums import EnemyState
from Enums import Direction
from SpriteSheet import SpriteSheet

class Enemy():
    def __init__(self, x, y, direction, objectHandler, window):
        # Init
        self.x = x
        self.y = y
        self.direction = direction
        self.objectHandler = objectHandler
        self.window = window
        self.width = 32 * self.window.scaleFactor
        self.height = 32 * self.window.scaleFactor

        # Personalized
        self.ID = 'Enemy'
        self.velX = 0
        self.velY = 0
        self.enemyState = EnemyState.WALKING
        self.player = None

        # Create Sprite Sheet
        self.spriteSheet = SpriteSheet('./assets/art/log.png')
        self._sprites = self.spriteSheet.getImageArray(32, 32, self.width, self.height)

        # Active Sprite
        self.activeSprite = self._sprites[0][0]

        # Collision
        self.colliderOffsetX = 32
        self.colliderOffsetY = 32
        self.colliderWidth = 64
        self.colliderHeight = 64
        self.collider = pygame.Rect(self.x + self.colliderOffsetX, self.y + self.colliderOffsetY, self.colliderWidth, self.colliderHeight)

        self.lastTick = 0
        self.animationFrame = 0
    
    def tick(self, ticks):
        # Set Player if not player
        if self.player == None:
            self.player = self.objectHandler.getObjectByID('Player')
        
        # Move Enemy if player in distance
        if math.sqrt((self.x - self.player.x) ** 2 + (self.y - self.player.y) ** 2) <= 5 * 16 * self.window.scaleFactor:
            self.enemyState = EnemyState.WALKING
            self.velX = (self.player.x - self.x) / 100
            self.velY = (self.player.y - self.y) / 100
        else:
            self.velX = 0
            self.velY = 0
            self.enemyState = EnemyState.IDLE
            self.animationFrame = 0

        # Set Direction To Moving
        if abs(self.velX) > abs(self.velY):
            if self.velX < 0: self.direction = Direction.LEFT
            elif self.velX > 0: self.direction = Direction.RIGHT
        elif abs(self.velY) > abs(self.velX):
            if self.velY < 0: self.direction = Direction.UP
            elif self.velY > 0: self.direction = Direction.DOWN
        
        if self.velX > 1: self.velX = 1
        if self.velX < -1: self.velX = -1
        if self.velY > 1: self.velY = 1
        if self.velY < -1: self.velY = -1

        self.x += self.velX
        self.y += self.velY

        self.collider.x = self.x + self.colliderOffsetX
        self.collider.y = self.y + self.colliderOffsetY

        self.animate(ticks)

    def render(self, scrollX, scrollY):
        # Render Enemy
        self.window.drawSprite(self.x - scrollX, self.y - scrollY, self.activeSprite)

    def animate(self, ticks):
        if self.enemyState == EnemyState.IDLE:
            if self.direction == Direction.UP:
                self.activeSprite = self._sprites[1][0]
            elif self.direction == Direction.LEFT:
                self.activeSprite = self._sprites[3][0]
            elif self.direction == Direction.DOWN:
                self.activeSprite = self._sprites[0][0]
            elif self.direction == Direction.RIGHT:
                self.activeSprite = self._sprites[2][0]
        elif self.enemyState == EnemyState.WALKING:
            if self.animationFrame == 0:
                self.lastTick = ticks
                self.animationFrame += 1
            if self.animationFrame == 1:
                if self.direction == Direction.UP: self.activeSprite = self._sprites[1][1]
                elif self.direction == Direction.LEFT: self.activeSprite = self._sprites[3][1]
                elif self.direction == Direction.DOWN: self.activeSprite = self._sprites[0][1]
                elif self.direction == Direction.RIGHT: self.activeSprite = self._sprites[2][1]
                elif self.direction == Direction.LEFT_UP: self.activeSprite = self._sprites[3][1]
                elif self.direction == Direction.LEFT_DOWN: self.activeSprite = self._sprites[3][1]
                elif self.direction == Direction.RIGHT_UP: self.activeSprite = self._sprites[2][1]
                elif self.direction == Direction.RIGHT_DOWN: self.activeSprite = self._sprites[2][1]
            elif self.animationFrame == 2:
                if self.direction == Direction.UP: self.activeSprite = self._sprites[1][2]
                elif self.direction == Direction.LEFT: self.activeSprite = self._sprites[3][2]
                elif self.direction == Direction.DOWN: self.activeSprite = self._sprites[0][2]
                elif self.direction == Direction.RIGHT: self.activeSprite = self._sprites[2][2]
                elif self.direction == Direction.LEFT_UP: self.activeSprite = self._sprites[3][2]
                elif self.direction == Direction.LEFT_DOWN: self.activeSprite = self._sprites[3][2]
                elif self.direction == Direction.RIGHT_UP: self.activeSprite = self._sprites[2][2]
                elif self.direction == Direction.RIGHT_DOWN: self.activeSprite = self._sprites[2][2]
            elif self.animationFrame == 3:
                if self.direction == Direction.UP: self.activeSprite = self._sprites[1][3]
                elif self.direction == Direction.LEFT: self.activeSprite = self._sprites[3][3]
                elif self.direction == Direction.DOWN: self.activeSprite = self._sprites[0][3]
                elif self.direction == Direction.RIGHT: self.activeSprite = self._sprites[2][3]
                elif self.direction == Direction.LEFT_UP: self.activeSprite = self._sprites[3][3]
                elif self.direction == Direction.LEFT_DOWN: self.activeSprite = self._sprites[3][3]
                elif self.direction == Direction.RIGHT_UP: self.activeSprite = self._sprites[2][3]
                elif self.direction == Direction.RIGHT_DOWN: self.activeSprite = self._sprites[2][3]
            elif self.animationFrame == 4:
                if self.direction == Direction.UP: self.activeSprite = self._sprites[1][0]
                elif self.direction == Direction.LEFT: self.activeSprite = self._sprites[3][0]
                elif self.direction == Direction.DOWN: self.activeSprite = self._sprites[0][0]
                elif self.direction == Direction.RIGHT: self.activeSprite = self._sprites[2][0]
                elif self.direction == Direction.LEFT_UP: self.activeSprite = self._sprites[3][0]
                elif self.direction == Direction.LEFT_DOWN: self.activeSprite = self._sprites[3][0]
                elif self.direction == Direction.RIGHT_UP: self.activeSprite = self._sprites[2][0]
                elif self.direction == Direction.RIGHT_DOWN: self.activeSprite = self._sprites[2][0]
            if ticks - self.lastTick == 20:
                self.lastTick = ticks
                self.animationFrame += 1
            if self.animationFrame == 5:
                self.animationFrame = 0