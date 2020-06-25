#!/usr/bin/python3
import uuid
import os
from datetime import datetime
import numpy as np
import random

import pygame
from pygame.locals import *


class Map():

    def __init__(self, width, height, tilesize):
        self.width = width
        self.height = height
        self.tilesize = tilesize
        self.tileset = ["tile_void.png", "tile.png",
                        "tile_wall.png", "tile_hole.png", "tile_unknown.png"]
        self.wtile = self.width // self.tilesize + 1
        self.htile = self.height // self.tilesize + 1
        self.mapmatrix = [[0 for i in range(self.htile)]
                          for i in range(self.wtile)]
        self.surface = pygame.Surface((self.width, self.height))

    def mapRandom(self):
        noise = generate_perlin_noise_2d((self.wtile, self.htile), (1, 1))
        for i in range(len(noise)):
            for j in range(len(noise[i])):
                n = noise[i][j]
                if n < 1 and n > -0.1 and self.mapmatrix[i][j] == 0:
                    n = 1
                    self.mapmatrix[i][j] = n

    def mapStructure(self):
        checkTiles = [(-1, -1), (-1, 0), (0, -1), (1, 0),
                      (0, 1), (1, 1), (-1, 1), (1, -1)]
        for i in range(len(self.mapmatrix)):
            for j in range(len(self.mapmatrix[0])):
                if self.mapmatrix[i][j] == 1:
                    try:
                        for k, l in checkTiles:
                            if self.mapmatrix[i + k][j + l] == 0:
                                self.mapmatrix[i + k][j + l] = 2
                    except:
                        pass
        for i in range(len(self.mapmatrix)):
            for j in range(len(self.mapmatrix[0])):
                if self.mapmatrix[i][j] == 2:
                    try:
                        c = 0
                        for k, l in checkTiles:
                            if self.mapmatrix[i + k][j + l] == 0:
                                c += 1
                                break
                        if c == 0:
                            self.mapmatrix[i][j] = 1
                    except:
                        pass
        for i in range(0, len(self.mapmatrix), len(self.mapmatrix) - 1):
            for j in range(0, len(self.mapmatrix), len(self.mapmatrix[0]) - 1):
                if self.mapmatrix[i][j] == 1:
                    self.mapmatrix[i][j] = 2

    def mapBuild(self):
        i = 0
        j = 0

        k = l = 0
        while i < self.width - 1:
            tile = Tile(self.tileset[self.mapmatrix[k][l]], (i, j))
            tile.draw(self.surface)
            while j < self.height - 1:
                tile = Tile(self.tileset[self.mapmatrix[k][l]], (i, j))
                tile.draw(self.surface)
                l += 1
                j += 64
            l = 0
            j = 0
            k += 1
            i += 64

    def mapPrint(self):
        for k in range(len(self.mapmatrix)):
            for l in range(len(self.mapmatrix[0])):
                print(self.mapmatrix[k][l], end="")
            print()


class Tile(pygame.sprite.Sprite):

    def __init__(self, fpath, position=(0, 0)):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', fpath))
        self.surf = pygame.Surface((64, 64))
        self.rect = self.surf.get_rect(x=position[0], y=position[1])

    def draw(self, surface):
        surface.blit(self.image, self.rect)


def generate_perlin_noise_2d(shape, res):
    def f(t):
        return 6*t**5 - 15*t**4 + 10*t**3

    delta = (res[0] / shape[0], res[1] / shape[1])
    d = (shape[0] // res[0], shape[1] // res[1])
    grid = np.mgrid[0:res[0]:delta[0], 0:res[1]
        :delta[1]].transpose(1, 2, 0) % 1
    # Gradients
    angles = 2*np.pi*np.random.rand(res[0]+1, res[1]+1)
    gradients = np.dstack((np.cos(angles), np.sin(angles)))
    g00 = gradients[0:-1, 0:-1].repeat(d[0], 0).repeat(d[1], 1)
    g10 = gradients[1:, 0:-1].repeat(d[0], 0).repeat(d[1], 1)
    g01 = gradients[0:-1, 1:].repeat(d[0], 0).repeat(d[1], 1)
    g11 = gradients[1:, 1:].repeat(d[0], 0).repeat(d[1], 1)
    # Ramps
    n00 = np.sum(np.dstack((grid[:, :, 0], grid[:, :, 1])) * g00, 2)
    n10 = np.sum(np.dstack((grid[:, :, 0]-1, grid[:, :, 1])) * g10, 2)
    n01 = np.sum(np.dstack((grid[:, :, 0], grid[:, :, 1]-1)) * g01, 2)
    n11 = np.sum(np.dstack((grid[:, :, 0]-1, grid[:, :, 1]-1)) * g11, 2)
    # Interpolation
    t = f(grid)
    n0 = n00*(1-t[:, :, 0]) + t[:, :, 0]*n10
    n1 = n01*(1-t[:, :, 0]) + t[:, :, 0]*n11
    return np.sqrt(2)*((1-t[:, :, 1])*n0 + t[:, :, 1]*n1)
