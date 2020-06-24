#!/usr/bin/python3
"""This is the console for COderz"""
import cmd
from models.entities.player import Player
from datetime import datetime
from shlex import split

class Coderz(cmd.Cmd):
    prompt = "(Coderz) "
    all_classes = {"Player"}
    def emptyline(self):
        pass

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def do_create(self, line):
        my_list = line.split(" ")
        y = 0
        dic = {}
        player = eval("{}()".format(my_list[0]))
        player.__dict__["name"] = my_list[1]
        player.__dict__["email"] = my_list[2]
        player.__dict__["password"] = my_list[3]
        #(player).__dict__.update(dic)
        #(player).save()
        print(player.__dict__)
        print("{}".format(player.id))
    def do_show(self, line):
        my_list = line.split(" ")
        objects = storage.all()
        
if __name__ == "__main__":
    Coderz().cmdloop()
