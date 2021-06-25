#!/usr/bin/python3
"""module of 'FileStorage' class"""

import os
import json
from models.base_model import BaseModel


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
        try:
            with open(self.__file_path, "r") as f:
                dict = json.load(f)
            for key in dict:
                self.__objects[key] = BaseModel(**dict[key])
        except:
            pass
