#!/usr/bin/python3
"""module of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User

white_list = ["BaseModel", "User"]
class_list = [BaseModel, User]


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
        elif args[0] not in white_list:
            print("** class doesn't exist **")
        else:
            for i in range(white_list):
                if args[i] == white_list[i]:
                    return
            new_instance = class_list[i]
            print(new_instance.id)
            new_instance.save()

    def do_show(self, line):
        """prints the string representation of an instance
           based on the class name and id"""
        args = line.split()
        objects_dic = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in white_list:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        elif args[0]+"."+args[1] in objects_dic:
            print(objects_dic[args[0]+"."+args[1]])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """deletes an instance based on the class name and id"""
        args = line.split()
        objects_dic = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in white_list:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        elif args[0]+"."+args[1] in objects_dic:
            storage.all().pop(args[0]+"."+args[1])
        else:
            print("** no instance found **")

    def do_all(self, line):
        """prints all string representation of all instances
           based (or not) on the class name"""
        args = line.split()
        objects_dic = storage.all()
        if len(args) == 0:
            for key in objects_dic:
                print(objects_dic[key])
        elif args[0] in white_list:
            for key in objects_dic:
                if objects_dic[key].__class__.__name__ == args[0]:
                    print(objects_dic[key])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """updates an instance based on the class name and id
           by adding or updating attribute"""
        args = line.split()
        objects_dic = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in white_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0]+"."+args[1] not in objects_dic:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            setattr(storage.all()[args[0]+"."+args[1]],
                    args[2], args[3])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
