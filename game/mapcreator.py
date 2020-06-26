#!/usr/bin/python3
import uuid
import os
from datetime import datetime
import numpy as np
import random
from settings import *


class MapGenerator():

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.tilesize = TILESIZE
        self.gridwidth = GRIDWIDTH
        self.gridheight = GRIDHEIGHT
        self.mapmatrix = [[0 for i in range(self.gridwidth)]
                          for i in range(self.gridheight)]
        self.fpath = "map.txt"

    def map_random(self):
        noise = generate_perlin_noise_2d(
            (self.gridwidth, self.gridheight), (1, 1))
        for i in range(len(noise)):
            for j in range(len(noise[i])):
                n = noise[i][j]
                try:
                    if n < 1 and n > -0.1 and self.mapmatrix[i][j] == 0:
                        n = 1
                        self.mapmatrix[i][j] = n
                except:
                    pass

    def map_structure(self):
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

        for i in range(len(self.mapmatrix)):
            for j in range(len(self.mapmatrix[0])):
                try:
                    if self.mapmatrix[i][j] == 1:
                        self.mapmatrix[i][j] = 4
                        break
                except:
                    self.mapmatrix[i][j] = 2
            break

    def map_to_file(self):
        np.savetxt(self.fpath, self.mapmatrix, fmt="%.0f", delimiter='')


def generate_perlin_noise_2d(shape, res):
    def f(t):
        return 6*t**5 - 15*t**4 + 10*t**3

    delta = (res[0] / shape[0], res[1] / shape[1])
    d = (shape[0] // res[0], shape[1] // res[1])
    grid = np.mgrid[0:res[0]:delta[0], 0:res[1]                    :delta[1]].transpose(1, 2, 0) % 1
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
