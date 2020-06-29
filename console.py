#!/usr/bin/python3
"""
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """exit the program"""
        return True

    def do_quit(self, line):
        """same as previous"""
        return True

    def emptyline(self):
        """does nothing"""
        pass


if __name__ == '__main':
    HBNBCommand().cmdloop()
