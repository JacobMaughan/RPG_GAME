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
                if self.player.collider.colliderect(tmpObject.collider):
                    if not tmpObject == self.player:
                        self.player.collide(tmpObject)

        # Scroll screen to player movement
        if self.objectState == GameState.GAME:
            self.scrollX += (self.player.x - self.scrollX - ((self.game.width - self.player.width) / 2)) / 20
            self.scrollY += (self.player.y - self.scrollY - ((self.game.height - self.player.height) / 2)) / 20

    
    def render(self):
        # Render all loaded objects
        for tmpObject in self._objects:
            tmpObject.render(self.scrollX, self.scrollY)
    
    # Add objects
    def addObject(self, objectToAdd):
        self._objects.append(objectToAdd)
    
    # Remove objects
    def removeObject(self, objectToRemove):
        for i in range(len(self._objects)):
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