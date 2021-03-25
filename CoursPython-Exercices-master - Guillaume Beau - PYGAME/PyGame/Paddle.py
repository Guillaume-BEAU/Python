import pygame
from pygame import draw
from GameObject import GameObject

class Paddle(GameObject):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.racketHeight = 80
        self.racketWidth = 20
        self.screen = None
        self.screenHeight = 600
        self.rectangle = None

    def init(self, screen):
        self.screen = screen
        self.rectangle = draw.rect(
            self.screen,  
            (255, 255, 255),  
            pygame.Rect(self.x, self.y, self.racketWidth, self.racketHeight)
        )

    def update(self):
        self.rectangle = draw.rect(
            self.screen,  
            (255, 255, 255), 
            pygame.Rect(self.x, self.y, self.racketWidth, self.racketHeight)
        )

    def setY(self, y):
        if self.y >= 0 and self.y <= self.screenHeight - self.racketHeight:
            self.y = y
        elif self.y < 0:
            self.y = 0
        elif self.y > self.screenHeight - self.racketHeight:
            self.y = self.screenHeight - self.racketHeight