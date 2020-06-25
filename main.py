#!/usr/bin/python3
from models.game import Game
from models.entities.player import Player

import time


import pygame
from pygame.locals import *

fps = 60
frameDelay = 1000 // fps


def run():
    pygame.init()
    game = Game("Coderz", (1000, 800))

    P1 = Player()

    while game.running:
        pygame.draw.circle(game.surface, 0, (200, 50), 30)
        game.update(P1)
        game.handle()
    return 0


if __name__ == "__main__":
    run()
