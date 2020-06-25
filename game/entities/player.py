#!/usr/bin/python3
import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

import pygame
from pygame.locals import *


Player = declarative_base()


class Player(pygame.sprite.Sprite):

    def __init__(self, name="", texpath=""):
        self.name = None
        self.id = str(uuid.uuid4())
        self.score = 0
        self.texture = {"head": "", "body": '', "feet": ""}
        self.email = ""
        self.password = ""

    def __str__(self):
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        return self.__str__()

    def save(self):
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in my_dict:
            my_dict.pop("_sa_instance_state")
        return my_dict

    def delete(self):
        models.storage.delete(self)

    def createTex(self):
        tmpSurf = sdl2.ext.load_image(self.__name)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
