#!/usr/bin/python3
import json
from os import path
from models.base_model import BaseModel

class FileStorage():
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.JSON"
    __objects = {}

    def all(self):
        """ returns a dictionary of obj.id: <val> """
        return FileStorage.__objects

    def new(self, obj):
        """ sets the instance: id pair in the dict __objects """
        FileStorage.__objects[self.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        """ serializes __objects to JSON file at __file_path """
        with open(FileStorage.__file_path, 'w') as fi:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            fi.write(json.dumps(d))

    def reload(self):
        """ deserializes JSON file at __file_path and stores into __objects """
        if (path.isfile(FileStorage.__file_path) == True):
            with open(FileStorage.__file_path) as fi:
                d = json.load(fi)
                FileStorage.__objects = {k: BaseModel(**v) for k, v in d.items()}
