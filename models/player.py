#!/usr/bin/python3
import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


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
