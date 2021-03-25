import pygame
from pygame import display, key
from pygame.constants import K_UP, K_DOWN, K_ESCAPE, K_z, K_s

from Ball import Ball
from GameObject import GameObject
from Paddle import Paddle


class Game(GameObject):

    def __init__(self):
        self.screenWidth = 800
        self.screenHeight = 600
        self.scorePlayer1 = 0
        self.scorePlayer2 = 0
        self.should_run = True
        self.screen = None
        self.ball = Ball(400, 300, self)
        racketWidth = 20
        racketHeight = 80
        self.racket1 = Paddle(0, self.screenHeight / 2 - racketHeight)
        self.racket2 = Paddle(self.screenWidth - racketWidth, self.screenHeight / 2 - racketHeight)

    def init(self, screen):
        self.screen = screen
        self.ball.init(screen)
        self.racket1.init(screen)
        self.racket2.init(screen)

    def update(self):
        self.displayPongInfo()
        self.displayScore()
        if (key.get_pressed()[K_ESCAPE]):
            self.should_run = False
        if (key.get_pressed()[K_z]):
            self.racket1.setY(self.racket1.y - 1)
        if (key.get_pressed()[K_s]):
            self.racket1.setY(self.racket1.y + 1)
        if (key.get_pressed()[K_UP]):
            self.racket2.setY(self.racket2.y - 1)
        if (key.get_pressed()[K_DOWN]):
            self.racket2.setY(self.racket2.y + 1)
        self.manageBallRacketsCollision()
        self.ball.update()
        self.racket1.update()
        self.racket2.update()

    def manageBallRacketsCollision(self):
        if self.ball.circle.colliderect(self.racket1.rectangle):
            self.ball.inverseDirectionX()
        if self.ball.circle.colliderect(self.racket2.rectangle):
            self.ball.inverseDirectionX()