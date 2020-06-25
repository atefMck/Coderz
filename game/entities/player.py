#!/usr/bin/python3
import uuid
import os
from datetime import datetime

import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'player.png'))
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect()

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 1000:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
