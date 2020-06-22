#!/usr/bin/python3
import sdl2
import sdl2.ext

WHITE = sdl2.ext.Color(255, 255, 255)


class Game():
    """docstring for BaseModel"""

    def __init__(self, name="No Name!", size=(800, 600)):
        try:
            self.__name = name
            self.__size = size
            sdl2.ext.init()
            self.window = sdl2.ext.Window(name, size)
            self.window.show()
            self.running = True
        except Exception as e:
            print(e)

    def update(self):
        self.window.refresh()

    def handle(self):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                self.running = False
                break

    def quit(self):
        sdl2.ext.quit()
