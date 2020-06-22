#!/usr/bin/python3
import ctypes
from models.game import Game
import sys
import sdl2
import sdl2.ext
import time

fps = 60
frameDelay = 1000 // fps


def run():
    game = Game("Coderz", (1000, 800))
    while game.running:
        frameStart = sdl2.SDL_GetTicks()
        game.handle()
        game.update()
        frameTime = sdl2.SDL_GetTicks() - frameStart
        if frameDelay > frameTime:
            sdl2.SDL_Delay(frameDelay - frameTime)
    game.quit()
    return 0


if __name__ == "__main__":
    sys.exit(run())
