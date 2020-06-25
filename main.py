#!/usr/bin/python3
from game.game import Game
from game.map.map import Map
from game.entities.player import Player

import time


import pygame
from pygame.locals import *

fps = 60
frameDelay = 1000 // fps


def run():
    pygame.init()
    game = Game("Coderz", (1024, 764))

    P1 = Player()
    level = Map(1000, 800, 64)
    level.mapRandom()
    level.mapStructure()
    level.mapBuild()
    level.mapPrint()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)

    while game.running:
        game.displaysurface.fill(0)
        level.mapBuild()
        for entity in all_sprites:
            game.displaysurface.blit(entity.image, entity.rect)
            entity.move()
        game.update(P1)
        game.handle()
    return 0


if __name__ == "__main__":
    run()
