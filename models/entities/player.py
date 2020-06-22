#!/usr/bin/python3


class Player():
    """docstring for BaseModel"""

    def __init__(self, name="", texpath=""):
        self.__texpath = texpath
        self.__name = name

    def createTex(self):
        tmpSurf = sdl2.ext.load_image(self.__name)
