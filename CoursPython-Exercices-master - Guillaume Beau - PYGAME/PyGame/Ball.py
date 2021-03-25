from pygame import draw

from GameObject import GameObject
from Direction import Direction


class Ball(GameObject):
    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.screenWidth = 800
        self.screenHeight = 600
        self.speed = 1
        self.direction = Direction(self.speed, self.speed)
        self.circle = None
        self.screen = None
        self.game = game

    def init(self, screen):
        self.screen = screen
        self.circle = draw.circle(
            self.screen,  
            (255, 255, 255),  
            (self.x, self.y),  
            5 # diamètre
        )

    def update(self):
        if self.x < 0:
            self.resetBall()
            self.game.scorePlayer2 = self.game.scorePlayer2 + 1
        if self.x > self.screenWidth:
            self.resetBall()
            self.game.scorePlayer1 = self.game.scorePlayer1 + 1
        if self.y < 0:
            self.inverseDirectionY()
        if self.y > self.screenHeight:
            self.inverseDirectionY()
        self.x += self.direction.getX()
        self.y += self.direction.getY()
        self.circle = draw.circle(
            self.screen,  
            (255, 255, 255), 
            (self.x, self.y), 
            15  # config diamètre
        )

    def inverseDirectionX(self):
        self.direction.x = -self.direction.x

    def inverseDirectionY(self):
        self.direction.y = -self.direction.y

    def resetBall(self):
        self.x = self.screenWidth / 2
        self.y = self.screenHeight / 2
