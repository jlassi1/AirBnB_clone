#!/usr/bin/python3
"""
python module
"""
import json
from models.base_model import BaseModel

from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place

class FileStorage:
    """storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        d = {}
        with open(self.__file_path, 'w+') as f:
            for k, v in self.__objects.items():
                d[k] = v.to_dict()
            json.dump(d, f)

    def reload(self):
        """deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
        except IOError:
            return
        new_dct = {}
        for key, val in new_obj.items():
            new_dct[key] = eval(val["__class__"])(**val)
        self.__objects = new_dct
