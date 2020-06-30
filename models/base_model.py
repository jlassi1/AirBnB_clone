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
        if kwargs is not None:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            for key, val in kwargs.items():
                if key is not "__class__":
                    if (key is "created_at" or key is "updated_at"):
                        val = datetime.strptime(val,
                                                "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

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
        dct = self.__dict__
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        dct.update({'__class__': type(self).__name__})
        return dct
