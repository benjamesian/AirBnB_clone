#!/usr/bin/python3
import json
from os import path

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
        FileStorage.__objects[self.__class__.__name__.id]

    def save(self):
        """ serializes __objects to JSON file at __file_path """
        with open(FileStorage.__file_path, 'w') as fi:
            fi.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """ deserializes JSON file at __file_path and stores into __objects """
        if (path.isfile(FileStorage.__file_path) == True):
            with open(FileStorage.__file_path) as fi:
                FileStorage.__objects = json.load(fi)
