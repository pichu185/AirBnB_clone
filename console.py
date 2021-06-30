#!/usr/bin/python3
"""module of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex

class_list = {"BaseModel": BaseModel,
              "User": User,
              "State": State,
              "City": City,
              "Amenity": Amenity,
              "Place": Place,
              "Review": Review
              }
white_list = []
for key in class_list:
    white_list.append(key)
int_atr = []
float_atr = []


class HBNBCommand(cmd.Cmd):
    """Representation of a HBNBCommand"""

    prompt = "(hbnb) "

    def emptyline(self):
        return False

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
            for key, value in class_list.items():
                if args[0] == key:
                    new_instance = value()
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
        objects_list = []
        if len(args) == 0:
            for key in objects_dic:
                objects_list.append(objects_dic[key].__str__())
            print(objects_list)
        elif args[0] in white_list:
            for key in objects_dic:
                if objects_dic[key].__class__.__name__ == args[0]:
                    objects_list.append(objects_dic[key].__str__())
            print(objects_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """updates an instance based on the class name and id
           by adding or updating attribute"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in class_list:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(storage.all()[k], args[2], args[3])
                            storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
        """
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
            key = args[0]+"."+args[1]
            attr = args[2]
            value = args[3]
            instance = objects_dic[key]
            if type(getattr(instance, attr)) is int:
                if (value).isnumeric():
                    value = int(value)
            elif type(getattr(instance, attr)) is float:
                idk = args[3].split(".")
                if idk[0].isnumeric() and idk[1].isnumeric():
                    value = float(value)
            setattr(storage.all()[key], attr, value)
        storage.all()[key].save()
        """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
