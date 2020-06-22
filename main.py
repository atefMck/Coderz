#!/usr/bin/python3
import ctypes
from models.game import Game
import sys
import sdl2
import sdl2.ext
import time


def run():
    game = Game("Coderz", (1000, 800))
    while game.running:
        game.handle()
        game.update()
    return 0


if __name__ == "__main__":
    sys.exit(run())
