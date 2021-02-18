# Description: Handles window creation and drawing
# Author: Jacob Maughan

# Lib Imports
import pygame

class Window():
    def __init__(self, width, height, title, iconPath):
        # Init
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        pygame.display.set_icon(pygame.image.load(iconPath))
    
    # Fill full screen
    def fillScreen(self, r, g, b):
        self.screen.fill((r, g, b))

    # Draw a rectangle to screen
    def drawRect(self, x, y, width, height, r, g, b):
        pygame.draw.rect(self.screen, (r, g, b), (x, y, width, height))
    
    # Draw a sprite to screen
    def drawSprite(self, x, y, width, height, image):
        self.screen.blit(image, (x, y, width, height))