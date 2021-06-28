#!/usr/bin/python3
"""module of the command interpreter"""

import cmd
import models
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    """Representation of a HBNBCommand"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        return True

    def do_create(self, line):
        """creates a new instance of BaseModel, saves it and prints the id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            print(new_instance.id)
            new_instance.save()
    
    def do_show(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        elif "BaseModel."+args[1] in models.storage.all():
            objects_dic = models.storage.all()
            print(objects_dic["BaseModel."+args[1]])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        elif "BaseModel."+args[1] in models.storage.all():
            models.storage.all().pop("BaseModel."+args[1])
        else:
            print("** no instance found **")

    def do_all(self, line):
        args = line.split()
        if len(args) == 0 or args[0] == "BaseModel":
            objects_dic = models.storage.all()
            for key in objects_dic:
                print(objects_dic[key])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif not ("BaseModel."+args[1] in models.storage.all()):
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            setattr(models.storage.all()["BaseModel."+args[1]], args[2], args[3])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
