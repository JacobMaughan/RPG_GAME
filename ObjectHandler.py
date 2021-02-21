# Description: Handles game objects
# Author: Jacob Maughan

# Local Imports
from Enums import GameState

class ObjectHandler():
    def __init__(self, game):
        # Init
        self._objects = []

        # Add game instance
        self.game = game
        
        # Setup state for object handler
        self.objectState = None

        # Setup player intance
        self.player = None

        # Setup screen scroll for camera movement
        self.scrollClampX = 0
        self.scrollClampY = 0
        self.scrollX = 0
        self.scrollY = 0

    def tick(self, ticks):
        # Check if game state changed and update object handler state
        if not self.objectState == self.game.state:
                self.objectState = self.game.state
                # Add player object to instance of player if in GAME state
                if self.objectState == GameState.GAME:
                    self.player = self.getObjectByID('Player')
        
        # Tick all loaded objects
        for tmpObject in self._objects:
            tmpObject.tick(ticks)
            # If in game state check for collision
            if self.objectState == GameState.GAME:
                if tmpObject.ID == 'Tile':
                    if tmpObject.hasCollision:
                        if self.player.collider.colliderect(tmpObject.collider):
                            self.player.collide(tmpObject)
                elif tmpObject.ID == 'NewZoneTrigger':
                    if self.player.collider.colliderect(tmpObject.collider):
                        tmpObject.loadNewZone()
                elif tmpObject.ID == 'Enemy':
                    if self.player.collider.colliderect(tmpObject.collider):
                        self.player.hit(tmpObject, ticks)

        # Scroll screen to player movement
        if self.objectState == GameState.GAME:
            self.scrollX += (self.player.x - self.scrollX - ((self.game.width - self.player.width) / 2)) / 100
            self.scrollY += (self.player.y - self.scrollY - ((self.game.height - self.player.height) / 2)) / 100

            if self.scrollX < 0: self.scrollX = 0
            if self.scrollX > self.scrollClampX: self.scrollX = self.scrollClampX
            if self.scrollY < 0: self.scrollY = 0
            if self.scrollY > self.scrollClampY: self.scrollY = self.scrollClampY

    def render(self):
        # Render all loaded objects
        for tmpObject in self._objects:
            tmpObject.render(self.scrollX, self.scrollY)
    
    # Add objects
    def addObject(self, objectToAdd):
        self._objects.append(objectToAdd)
    
    # Remove objects
    def removeObject(self, objectToRemove):
        for i in range(len(self._objects) - 1):
            if self._objects[i] == objectToRemove:
                self._objects.pop(i)
    
    # Remove all objects
    def clearObjects(self):
        self._objects = []
    
    # Get object by its id, I.E 'Player'
    def getObjectByID(self, ID):
        for i in range(len(self._objects)):
            if self._objects[i].ID == ID:
                return self._objects[i]
    
    def getCollision(self, collider):
        returnObjects = []
        for tmpObject in self._objects:
            if collider.colliderect(tmpObject.collider):
                returnObjects.append(tmpObject)
        return returnObjects

    def setScrollClamp(self, scrollClampX, scrollClampY):
        self.scrollClampX = scrollClampX - self.game.width
        self.scrollClampY = scrollClampY - self.game.height