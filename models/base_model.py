#!/usr/bin/python3
"""
"""
import uuid
from datetime import datetime


class BaseModel():
    """ """
    def __init__(self):
        """ """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__ )

    def save(self):
        """ """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """ """
        dct = self.__dict__
        self.created_at = datetime.now().isoformat("T")
        self.updated_at = datetime.now().isoformat("T")
        dct.update({'__class__': type(self).__name__})
        return dct