#!/usr/bin/python3
"""
python module
"""
import cmd
from models.base_model import BaseModel
import shlex
from models.engine.file_storage import FileStorage


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

    def do_create(self, line):
        """ creates new instances """
        comm = shlex.split(line)
        if len(line) == 0:
            print('** class name missing **')
        elif line in "BaseModel":
            new_inst = eval(comm[0])()
            new_inst.save()
            print(new_inst.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ Prints the string representation of an instance """
        comm = shlex.split(line)
        if len(comm) == 0:
            print('** class name missing **')
        elif comm[0] not in "BaseModel":
            print("** class doesn't exist **")
        elif len(comm) == 1:
            print("** instance id missing **")
        else:
            instance = comm[0] + '.' + comm[1]
            if instance in storage.all():
                print(storage.all()[instance])
            else:
                print('** no instance found **')

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        comm = shlex.split(line)
        if len(comm) == 0:
            print('** class name missing **')
        elif comm[0] not in "BaseModel":
            print("** class doesn't exist **")
        elif len(comm) == 1:
            print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
