#!/usr/bin/python3
"""
python module
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """ Base class"""
    def __init__(self, *args, **kwargs):
        """ Initialization """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        val = datetime.strptime(val,
                                                "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)

    def __str__(self):
        """the forma of sting return """
        return "[{}] ({}) {}".format(
            type(self).__name__,
            self.id,
            self.__dict__)

    def save(self):
        """save instance """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ method to generate a dictionary representation of an instance """
        dct = dict(self.__dict__)
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct
