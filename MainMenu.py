# Description: The main menu object
# Author: Jacob Maughan

# Lib Imports
import pygame

# Local Imports
from Enums import Direction
from Enums import GameState

class MainMenu():
    def __init__(self, game, window):
        # Init
        self.game = game
        self.window = window
        
        # Personalized
        self.ID = 'Menu'

        # Background Image
        self.backgroundImage = pygame.image.load('./assets/art/background.png')
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (self.window.screen.get_width(), self.window.screen.get_height()))

        # Font
        self.font = pygame.font.SysFont('Arial Black', 60)

        self.selected = 0
    
    def tick(self, ticks):
        pass

    def render(self, scrollX, scrollY):
        self.window.drawSprite(0, 0, self.backgroundImage)
        if self.selected == 0:
            self.window.drawTextColored(self.window.screen.get_width() * 0.1, self.window.screen.get_height() * 0.1, 'Play', self.font, 255, 0, 0)
            self.window.drawText(self.window.screen.get_width() * 0.1, self.window.screen.get_height() * 0.75, 'Quit', self.font)
        if self.selected == 1:
            self.window.drawText(self.window.screen.get_width() * 0.1, self.window.screen.get_height() * 0.1, 'Play', self.font)
            self.window.drawTextColored(self.window.screen.get_width() * 0.1, self.window.screen.get_height() * 0.75, 'Quit', self.font, 255, 0, 0)
    
    def select(self, direction):
        if direction == Direction.DOWN:
            self.selected += 1
            if self.selected == 2: self.selected = 0
        elif direction == Direction.UP:
            self.selected -= 1
            if self.selected == -1: self.selected = 1
    
    def selectOption(self):
        if self.selected == 0:
            self.game.state = GameState.GAME
        if self.selected == 1:
            self.game.stop()