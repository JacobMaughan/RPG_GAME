# Description: The player object
# Author: Jacob Maughan

# Lib Imports
import pygame

# Local Imports
from Enums import Direction
from Enums import PlayerState
from JsonHandler import JsonHandler
from SpriteSheet import SpriteSheet

class Player():
    def __init__(self, scaleFactor, window):
        # Init
        self.scaleFactor = scaleFactor
        self.window = window

        # Personalized
        self.playerFile = JsonHandler('./assets/data/player.json')
        self.playerData = self.playerFile.getJson()

        self.ID = 'Player'
        self.width = 16 * self.scaleFactor
        self.height = 32 * self.scaleFactor
        self.velX = 0
        self.velY = 0
        self.x = self.playerData['x']
        self.y = self.playerData['y']
        self.speed = self.playerData['speed']
        self.health = self.playerData['health']
        self.maxHealth = self.playerData['maxHealth']

        # State
        self.playerState = PlayerState.IDLE
        self.direction = Direction(self.playerData['direction'])
        
        # Creating Spritesheet
        self.spriteSheet = SpriteSheet('./assets/art/character.png')

        # Loading sprites into array
        self._sprites = [[]]
        spriteY = 0
        y = 0
        while spriteY < 256:
            spriteX = 0
            x = 0
            while x < 272:
                self._sprites[y].append(self.spriteSheet.getImage(spriteX, spriteY ,16, 32))
                self._sprites[y][x] = pygame.transform.scale(self._sprites[y][x], (self.width, self.height))
                spriteX += 16
                x += 1
            self._sprites.append([])
            spriteY += 32
            y += 1

        # Active sprites
        self.activeSprite = None

        # Collision | Must set offsets for main collider
        self.colliderOffsetX = 20
        self.colliderOffsetY = 90

        self.swordColliderOffsetX = [0, -5, 0, 45]
        self.swordColliderOffsetY = [25, 50, 90, 50]

        self.collider = pygame.Rect(self.x + self.colliderOffsetX, self.y + self.colliderOffsetY, 25, 10)
        self.topCollider = pygame.Rect(self.collider.x + self.collider.width * 0.1, self.collider.y, self.collider.width * 0.8, self.collider.height * 0.1)
        self.leftCollider = pygame.Rect(self.collider.x, self.collider.y + self.collider.height * 0.1, self.collider.width * 0.1, self.collider.height * 0.8)
        self.bottomCollider = pygame.Rect(self.collider.x + self.collider.width * 0.1, self.collider.y + self.collider.height * 0.9, self.collider.width * 0.8, self.collider.height * 0.1)
        self.rightCollider = pygame.Rect(self.collider.x + self.collider.width * 0.9, self.collider.y + self.collider.height * 0.1, self.collider.width * 0.1, self.collider.height * 0.8)

        self.swordColliderTop = pygame.Rect(self.x + self.swordColliderOffsetX[0], self.y + self.swordColliderOffsetY[0], self.width, 30)
        self.swordColliderLeft = pygame.Rect(self.x + self.swordColliderOffsetX[1], self.y + self.swordColliderOffsetY[1], 30, 50)
        self.swordColliderBottom = pygame.Rect(self.x + self.swordColliderOffsetX[2], self.y + self.swordColliderOffsetY[2], self.width, 30)
        self.swordColliderRight = pygame.Rect(self.x + self.swordColliderOffsetX[3], self.y + self.swordColliderOffsetY[3], 30, 50)

        self.lastTick = 0
        self.animationFrame = 0

    def tick(self, ticks):
        # Check if moving and set player state
        if self.playerState == PlayerState.IDLE:
            if not self.velX == 0 or not self.velY == 0:
                self.playerState = PlayerState.WALKING

        # Move player by vel and set player state if stopped walking
        if self.playerState == PlayerState.WALKING:
            self.x += self.velX * self.speed
            self.y += self.velY * self.speed
            if self.velX == 0 and self.velY == 0:
                self.playerState = PlayerState.IDLE
        
        # Set collider's to x and y value
        self.collider.x = self.x + self.colliderOffsetX
        self.collider.y = self.y + self.colliderOffsetY

        self.swordColliderTop.x = self.x + self.swordColliderOffsetX[0]
        self.swordColliderTop.y = self.y + self.swordColliderOffsetY[0]
        self.swordColliderLeft.x = self.x + self.swordColliderOffsetX[1]
        self.swordColliderLeft.y = self.y + self.swordColliderOffsetY[1]
        self.swordColliderBottom.x = self.x + self.swordColliderOffsetX[2]
        self.swordColliderBottom.y = self.y + self.swordColliderOffsetY[2]
        self.swordColliderRight.x = self.x + self.swordColliderOffsetX[3]
        self.swordColliderRight.y = self.y + self.swordColliderOffsetY[3]

        # Animate player
        self.animate(ticks)

    def render(self, scrollX, scrollY):
        # Render Collider on bottom
        #self.window.drawRect(self.collider.x - scrollX, self.collider.y - scrollY, self.collider.width, self.collider.height, 0, 0, 255)

        # Render Sprite
        self.window.drawSprite(self.x - scrollX, self.y - scrollY, self.width, self.height, self.activeSprite)

        # Render Collider on top
        #self.window.drawRect(self.collider.x - scrollX, self.collider.y - scrollY, self.collider.width, self.collider.height, 0, 0, 255)
        #self.window.drawRect(self.swordColliderTop.x - scrollX, self.swordColliderTop.y - scrollY, self.swordColliderTop.width, self.swordColliderTop.height, 0, 0, 255)
        #self.window.drawRect(self.swordColliderBottom.x - scrollX, self.swordColliderBottom.y - scrollY, self.swordColliderBottom.width, self.swordColliderBottom.height, 0, 0, 255)
        #self.window.drawRect(self.swordColliderLeft.x - scrollX, self.swordColliderLeft.y - scrollY, self.swordColliderLeft.width, self.swordColliderLeft.height, 0, 0, 255)
        #self.window.drawRect(self.swordColliderRight.x - scrollX, self.swordColliderRight.y - scrollY, self.swordColliderRight.width, self.swordColliderRight.height, 0, 0, 255)
    
    # Check Animation
    def animate(self, ticks):
        if self.playerState == PlayerState.IDLE:
            if self.direction == Direction.UP:
                self.activeSprite = self._sprites[2][0]
            elif self.direction == Direction.LEFT:
                self.activeSprite = self._sprites[3][0]
            elif self.direction == Direction.DOWN:
                self.activeSprite = self._sprites[0][0]
            elif self.direction == Direction.RIGHT:
                self.activeSprite = self._sprites[1][0]
        if self.playerState == PlayerState.WALKING:
            if self.animationFrame == 0:
                self.lastTick = ticks
                self.animationFrame += 1
            if self.animationFrame == 1:
                if self.direction == Direction.UP: self.activeSprite = self._sprites[2][1]
                elif self.direction == Direction.LEFT: self.activeSprite = self._sprites[3][1]
                elif self.direction == Direction.DOWN: self.activeSprite = self._sprites[0][1]
                elif self.direction == Direction.RIGHT: self.activeSprite = self._sprites[1][1]
                elif self.direction == Direction.LEFT_UP: self.activeSprite = self._sprites[3][1]
                elif self.direction == Direction.LEFT_DOWN: self.activeSprite = self._sprites[3][1]
                elif self.direction == Direction.RIGHT_UP: self.activeSprite = self._sprites[1][1]
                elif self.direction == Direction.RIGHT_DOWN: self.activeSprite = self._sprites[1][1]
            elif self.animationFrame == 2:
                if self.direction == Direction.UP: self.activeSprite = self._sprites[2][2]
                elif self.direction == Direction.LEFT: self.activeSprite = self._sprites[3][2]
                elif self.direction == Direction.DOWN: self.activeSprite = self._sprites[0][2]
                elif self.direction == Direction.RIGHT: self.activeSprite = self._sprites[1][2]
                elif self.direction == Direction.LEFT_UP: self.activeSprite = self._sprites[3][2]
                elif self.direction == Direction.LEFT_DOWN: self.activeSprite = self._sprites[3][2]
                elif self.direction == Direction.RIGHT_UP: self.activeSprite = self._sprites[1][2]
                elif self.direction == Direction.RIGHT_DOWN: self.activeSprite = self._sprites[1][2]
            elif self.animationFrame == 3:
                if self.direction == Direction.UP: self.activeSprite = self._sprites[2][3]
                elif self.direction == Direction.LEFT: self.activeSprite = self._sprites[3][3]
                elif self.direction == Direction.DOWN: self.activeSprite = self._sprites[0][3]
                elif self.direction == Direction.RIGHT: self.activeSprite = self._sprites[1][3]
                elif self.direction == Direction.LEFT_UP: self.activeSprite = self._sprites[3][3]
                elif self.direction == Direction.LEFT_DOWN: self.activeSprite = self._sprites[3][3]
                elif self.direction == Direction.RIGHT_UP: self.activeSprite = self._sprites[1][3]
                elif self.direction == Direction.RIGHT_DOWN: self.activeSprite = self._sprites[1][3]
            elif self.animationFrame == 4:
                if self.direction == Direction.UP: self.activeSprite = self._sprites[2][0]
                elif self.direction == Direction.LEFT: self.activeSprite = self._sprites[3][0]
                elif self.direction == Direction.DOWN: self.activeSprite = self._sprites[0][0]
                elif self.direction == Direction.RIGHT: self.activeSprite = self._sprites[1][0]
                elif self.direction == Direction.LEFT_UP: self.activeSprite = self._sprites[3][0]
                elif self.direction == Direction.LEFT_DOWN: self.activeSprite = self._sprites[3][0]
                elif self.direction == Direction.RIGHT_UP: self.activeSprite = self._sprites[1][0]
                elif self.direction == Direction.RIGHT_DOWN: self.activeSprite = self._sprites[1][0]
            if ticks - self.lastTick == 20:
                self.lastTick = ticks
                self.animationFrame += 1
            if self.animationFrame == 5:
                self.animationFrame = 0
        elif self.playerState == PlayerState.ATTACKING:
            if self.animationFrame == 0:
                self.lastTick = ticks
                self.animationFrame += 1
            if self.animationFrame == 1:
                if self.direction == Direction.UP: self.activeSprite = self._sprites[5][0]
                elif self.direction == Direction.LEFT: self.activeSprite = self._sprites[7][0]
                elif self.direction == Direction.DOWN: self.activeSprite = self._sprites[4][0]
                elif self.direction == Direction.RIGHT: self.activeSprite = self._sprites[6][0]
                elif self.direction == Direction.LEFT_UP: self.activeSprite = self._sprites[7][0]
                elif self.direction == Direction.LEFT_DOWN: self.activeSprite = self._sprites[7][0]
                elif self.direction == Direction.RIGHT_UP: self.activeSprite = self._sprites[6][0]
                elif self.direction == Direction.RIGHT_DOWN: self.activeSprite = self._sprites[6][0]
            elif self.animationFrame == 2:
                if self.direction == Direction.UP: self.activeSprite = self._sprites[5][1]
                elif self.direction == Direction.LEFT: self.activeSprite = self._sprites[7][1]
                elif self.direction == Direction.DOWN: self.activeSprite = self._sprites[4][1]
                elif self.direction == Direction.RIGHT: self.activeSprite = self._sprites[6][1]
                elif self.direction == Direction.LEFT_UP: self.activeSprite = self._sprites[7][1]
                elif self.direction == Direction.LEFT_DOWN: self.activeSprite = self._sprites[7][1]
                elif self.direction == Direction.RIGHT_UP: self.activeSprite = self._sprites[6][1]
                elif self.direction == Direction.RIGHT_DOWN: self.activeSprite = self._sprites[6][1]
            elif self.animationFrame == 3:
                if self.direction == Direction.UP: self.activeSprite = self._sprites[5][2]
                elif self.direction == Direction.LEFT: self.activeSprite = self._sprites[7][2]
                elif self.direction == Direction.DOWN: self.activeSprite = self._sprites[4][2]
                elif self.direction == Direction.RIGHT: self.activeSprite = self._sprites[6][2]
                elif self.direction == Direction.LEFT_UP: self.activeSprite = self._sprites[7][2]
                elif self.direction == Direction.LEFT_DOWN: self.activeSprite = self._sprites[7][2]
                elif self.direction == Direction.RIGHT_UP: self.activeSprite = self._sprites[6][2]
                elif self.direction == Direction.RIGHT_DOWN: self.activeSprite = self._sprites[6][2]
            elif self.animationFrame == 4:
                if self.direction == Direction.UP: self.activeSprite = self._sprites[5][3]
                elif self.direction == Direction.LEFT: self.activeSprite = self._sprites[7][3]
                elif self.direction == Direction.DOWN: self.activeSprite = self._sprites[4][3]
                elif self.direction == Direction.RIGHT: self.activeSprite = self._sprites[6][3]
                elif self.direction == Direction.LEFT_UP: self.activeSprite = self._sprites[7][3]
                elif self.direction == Direction.LEFT_DOWN: self.activeSprite = self._sprites[7][3]
                elif self.direction == Direction.RIGHT_UP: self.activeSprite = self._sprites[6][3]
                elif self.direction == Direction.RIGHT_DOWN: self.activeSprite = self._sprites[6][3]
            if self.animationFrame == 5:
                if not self.velX == 0 or not self.velY == 0:
                    self.playerState = PlayerState.WALKING
                else:
                    self.playerState = PlayerState.IDLE
                self.animationFrame = 0
            else:
                if ticks - self.lastTick == 5:
                    self.lastTick = ticks
                    self.animationFrame += 1
    
    def move(self, isKeyDown, velX, velY):
        if isKeyDown:
            if velY == -1:
                self.velY = -1
                self.animationFrame = 0
                if self.velX == -1: self.direction = Direction.LEFT_UP
                elif self.velX == 1: self.direction = Direction.RIGHT_UP
                else: self.direction = Direction.UP
            if velX == -1:
                self.velX = -1
                self.animationFrame = 0
                if self.velY == -1: self.player = Direction.LEFT_UP
                elif self.velY == 1: self.player = Direction.LEFT_DOWN
                else: self.direction = Direction.LEFT
            if velY == 1:
                self.velY = 1
                self.animationFrame = 0
                if self.velX == -1: self.direction = Direction.LEFT_DOWN
                elif self.velX == 1: self.direction = Direction.RIGHT_DOWN
                else: self.direction = Direction.DOWN
            if velX == 1:
                self.velX = 1
                self.animationFrame = 0
                if self.velY == -1: self.direction = Direction.RIGHT_UP
                elif self.velY == 1: self.direction = Direction.RIGHT_DOWN
                else: self.direction = Direction.RIGHT
        else:
            if velX == 1:
                self.velX = 0
                if self.velY == -1: self.direction = Direction.UP
                elif self.velY == 1: self.direction = Direction.DOWN
            if velY == 1:
                self.velY = 0
                if self.velX == -1: self.direction = Direction.LEFT
                elif self.velX == 1: self.direction = Direction.RIGHT
            self.animationFrame = 0
    
    # Attack
    def attack(self, objectHandler):
        self.animationFrame = 0
        self.playerState = PlayerState.ATTACKING
        if self.direction == Direction.UP:
            collideObjects = objectHandler.getCollision(self.swordColliderTop)
            if not collideObjects == []:
                for tmpObject in collideObjects:
                    if tmpObject.ID == 'Enemy':
                        tmpObject.hit = True
        elif self.direction == Direction.LEFT or self.direction == Direction.LEFT_DOWN or self.direction == Direction.LEFT_UP:
            collideObjects = objectHandler.getCollision(self.swordColliderLeft)
            if not collideObjects == []:
                for tmpObject in collideObjects:
                    if tmpObject.ID == 'Enemy':
                        tmpObject.hit = True
        elif self.direction == Direction.DOWN:
            collideObjects = objectHandler.getCollision(self.swordColliderBottom)
            if not collideObjects == []:
                for tmpObject in collideObjects:
                    if tmpObject.ID == 'Enemy':
                        tmpObject.hit = True
        elif self.direction == Direction.RIGHT or self.direction == Direction.RIGHT_DOWN or self.direction == Direction.RIGHT_UP:
            collideObjects = objectHandler.getCollision(self.swordColliderRight)
            if not collideObjects == []:
                for tmpObject in collideObjects:
                    if tmpObject.ID == 'Enemy':
                        tmpObject.hit = True

    # Recieves detected collision
    def collide(self, collision):
        # Updates positions of side collisions
        self.topCollider.x = self.collider.x + self.collider.width * 0.1
        self.topCollider.y = self.collider.y

        self.leftCollider.x = self.collider.x
        self.leftCollider.y = self.collider.y + self.collider.height * 0.1

        self.bottomCollider.x = self.collider.x + self.collider.width * 0.1
        self.bottomCollider.y = self.collider.y + self.collider.height * 0.9

        self.rightCollider.x = self.collider.x + self.collider.width * 0.9
        self.rightCollider.y = self.collider.y + self.collider.height * 0.1

        if(self.topCollider.colliderect(collision.collider)):
            self.y = collision.y + collision.height - self.colliderOffsetY
        if(self.leftCollider.colliderect(collision.collider)):
            self.x = collision.x + collision.width - self.colliderOffsetX
        if(self.bottomCollider.colliderect(collision.collider)):
            self.y = collision.y - self.collider.height - self.colliderOffsetY
        if(self.rightCollider.colliderect(collision.collider)):
            self.x = collision.x - self.collider.width - self.colliderOffsetX
    
    def saveSettings(self):
        self.playerData['x'] = self.x
        self.playerData['y'] = self.y
        self.playerData['direction'] = self.direction.value
        self.playerData['speed'] = self.speed
        self.playerData['health'] = self.health
        self.playerData['maxHealth'] = self.maxHealth
        self.playerFile.saveJson(self.playerData)