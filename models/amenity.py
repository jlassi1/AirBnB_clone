#!/usr/bin/python3
"""
python module
"""
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


class Amenity(BaseModel):
    """Class Amenity"""
    name = ""
