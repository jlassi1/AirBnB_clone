#!/usr/bin/python3
"""
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """does nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
