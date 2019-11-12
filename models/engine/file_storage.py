#!/usr/bin/python3
"""File storage.

This module defines a class `FileStorage` that is capable of serializing
application objects and storing them in files for later retreival.

"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """
    Serializes instances to a JSON file and deserializes JSON file to
    instances.
    """

    __file_path = "file.JSON"
    __objects = {}

    def all(self):
        """ returns a dictionary of obj.id: <val> """
        return FileStorage.__objects

    def new(self, obj):
        """ sets the instance: id pair in the dict __objects """
        FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """ serializes __objects to JSON file at __file_path """
        with open(FileStorage.__file_path, 'w') as fi:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            fi.write(json.dumps(d))

    def reload(self):
        """ deserializes JSON file at __file_path and stores into __objects """
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path) as fi:
                d = json.load(fi)
                # FileStorage.__objects =\
                #     {k: BaseModel(**v) for k, v in d.items()}
                FileStorage.__objects = {}
                for k, v in d.items():
                    if k.startswith('BaseModel.'):
                        FileStorage.__objects[k] = BaseModel(**v)
                    elif k.startswith('User.'):
                        FileStorage.__objects[k] = User(**v)
                    elif k.startswith('Place.'):
                        FileStorage.__objects[k] = Place(**v)
                    elif k.startswith('State.'):
                        FileStorage.__objects[k] = State(**v)
                    elif k.startswith('City.'):
                        FileStorage.__objects[k] = City(**v)
                    elif k.startswith('Amenity.'):
                        FileStorage.__objects[k] = Amenity(**v)
                    elif k.startswith('Review.'):
                        FileStorage.__objects[k] = Review(**v)
