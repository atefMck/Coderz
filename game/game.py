#!/usr/bin/python3
from models.entities.player import Player

import sys

import pygame
from pygame.locals import *


class Game():
    """docstring for BaseModel"""

    def __init__(self, name="No Name!", size=(800, 600)):
        self.__name = name
        self.__size = size
        self.running = True
        self.surface = pygame.display.set_mode(self.__size)
        pygame.display.set_caption(self.__name)
        FPS = pygame.time.Clock()
        FPS.tick(60)

    def update(self, entity):
        entity.update()
        entity.draw(self.surface)
        pygame.display.update()

    def handle(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
