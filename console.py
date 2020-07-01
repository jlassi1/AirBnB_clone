#!/usr/bin/python3
"""
python module
"""
import cmd
from models.base_model import BaseModel
import shlex
from models import storage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = "(hbnb) "
    classs = [
        "BaseModel",
        "State",
        "City",
        "Place",
        "Review",
        "Amenity",
        "User"]

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
        elif line in HBNBCommand.classs:
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
        elif comm[0] not in HBNBCommand.classs:
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
        elif comm[0] not in HBNBCommand.classs:
            print("** class doesn't exist **")
        elif len(comm) == 1:
            print("** instance id missing **")
        else:
            instance = comm[0] + '.' + comm[1]
            if instance in storage.all():
                del storage.all()[instance]
                storage.save()
            else:
                print('** no instance found **')

    def do_all(self, line):
        """ Prints all string representation of all instances """
        comm = shlex.split(line)
        if len(comm) == 0:
            o_list = []
            for k in storage.all():
                s = str(storage.all()[k])
                o_list.append(s)
            print(o_list)
        elif comm[0] in self.classs:
            o_list = []
            for k in storage.all():
                if comm[0] in k:
                    s = str(storage.all()[k])
                    o_list.append(s)
            print(o_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ Updates an instance based on the class name and id """
        comm = shlex.split(line)
        if len(comm) == 0:
            print("** class name missing **")
        elif comm[0] not in HBNBCommand.classs:
            print("** class doesn't exist **")
        elif len(comm) == 1:
            print("** instance id missing **")
        elif len(comm) == 2:
            print("** attribute name missing **")
        elif len(comm) == 3:
            print("** value missing **")
        elif comm[0] + '.' + comm[1] not in storage.all():
            print("** no instance found **")
        else:
            ins = comm[0] + '.' + comm[1]
            setattr(storage.all()[ins], comm[2], comm[3])
            storage.all()[ins].save()

    def do_default(self, line):
        """ retrieve input """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
