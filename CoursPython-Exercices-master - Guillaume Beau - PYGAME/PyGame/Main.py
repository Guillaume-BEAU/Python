import pygame
from pygame import display
from Game import Game


def main():
    pygame.init()
    display.set_caption("Pong")
    screen = display.set_mode((800, 600))
    
    game = Game()
    game.init(screen)

    while game.should_run:
        screen.fill((0, 0, 0))
        game.update()
        display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.should_run = False

if __name__ == "__main__":
    main()