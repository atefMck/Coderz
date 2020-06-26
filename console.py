#!/usr/bin/python3
import json
from shlex import split
from datetime import datetime
from models.player import User
from models.player import Player
"""This is the console for COderz"""
import cmd


def check():

   with open("./web-app/data.json", "r") as f:
        s = f.read()
   if (s == ""):
        return True
    else:
        return False


class Coderz(cmd.Cmd):
    prompt = "(Coderz) "

    def emptyline(self):
        pass

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def do_create(self, line):
        exist = True
        my_list = line.split(" ")
        y = 0
        dic = {}
        player = eval("{}()".format(my_list[0]))

        try:
            player.__dict__["name"] = my_list[1]
            player.__dict__["email"] = my_list[2]
            player.__dict__["password"] = my_list[3]
        except:
            print("Usage: create Player <GamerTag> <email> <Password>")

        with open("./web-app/data.json", 'r') as f:
            jsondata = (f.read())
            jsn = '{{"data": [{}]}}'.format(jsondata)
            jsn = json.loads(jsn)
            for i in jsn["data"]:
                for k, v in i.items():
                    print(i["name"])
                    if i["name"] == my_list[1]:
                        print("already existing name")
                        exist = False
                        break
                    else:
                        exist = True

        checks = check()
        if exist:
            with open("./web-app/data.json", "a") as f:
                if checks:
                    f.write("{}".format(json.dumps(player.__dict__)))
                else:
                    f.write(" ,{}".format(json.dumps(player.__dict__)))

    def do_show(self, line):
        my_list = line.split(" ")
        if len(my_list) == 1:

            with open("./web-app/data.json", 'r') as f:
                print(json.loads('{{"data": [{}]}}'.format(f.read())))


if __name__ == "__main__":
    Coderz().cmdloop()
