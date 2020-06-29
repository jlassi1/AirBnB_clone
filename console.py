#!/usr/bin/python3
"""
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ """
    prompt = '(hbnb)'

    def do__EOF(self, line):
        """ """
        return True

    def do__quit(self, line):
        """ """
        return True


if __name__ == '__main':
    HBNBCommand().cmdloop()
