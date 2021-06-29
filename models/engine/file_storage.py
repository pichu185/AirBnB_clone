#!/usr/bin/python3
"""module of 'FileStorage' class"""

import os.path
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

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


class FileStorage():
    """Representation of a FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """class constructor"""
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__+"."+obj.id
        self.__objects.update({key: obj})

    def save(self):
        dict = {}
        for key in self.__objects:
            dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dict, f)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                dict = json.load(f)
            for key in dict:
                for key, value in class_list.items():
                    if key.__class__.__name__ == key:
                        self.__objects[key] = value(**dict[key])
                        return    
        else:
            pass
