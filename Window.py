# Description: Handles window creation and drawing
# Author: Jacob Maughan

# Lib Imports
import pygame

class Window():
    def __init__(self, scaleFactor, width, height, title, iconPath):
        # Init
        self.scaleFactor = scaleFactor
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
    def drawSprite(self, x, y, image):
        self.screen.blit(image, (x, y))
    
    def drawText(self, x, y, text, size):
        font = pygame.font.SysFont('./assets/fonts/BitScript.ttf', size)
        textImage = font.render(text, True, (0, 0, 0))
        self.screen.blit(textImage, (x, y))
