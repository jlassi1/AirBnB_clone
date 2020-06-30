#!/usr/bin/python3
"""
"""
import cmd
from models.base_model import BaseModel
import shlex


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """exit the program"""
        print()
        return True

    def do_quit(self, line):
        """same as previous"""
        return True

    def emptyline(self):
        """does nothing"""
        pass

    def do_create(self, arg):
        """ """
        comm = shlex.split(arg)
        if len(arg) == 0:
            print('** class name missing **')
        elif arg in self.classes:
            new_instance = eval(comm[0])()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ """
        comm = shlex.split(arg)
        if len(comm) == 0:
            print('** class name missing **')
        elif comm[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(comm) == 1:
            print("** instance id missing **")
        else:
            instance = comm[0] + '.' + comm[1]
            if instance in models.storage.all():
                print(models.storage.all()[instance])
            else:
                print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
