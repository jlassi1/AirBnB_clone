#!/usr/bin/python3
"""
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """ """
    def __init__(self, *args, **kwargs):
        """ """
        if kwargs is not None:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.now()
            for key, val in kwargs.items():
                if (key == "created_at" or key == "updated_at"):
                    val = datetime.strptime(val,
                                            "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        """the forma of sting return"""
        return "[{}] ({}) {}".format(
            type(self).__name__,
            self.id,
            self.__dict__)

    def save(self):
        """ """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ """
        dct = self.__dict__
        self.created_at = datetime.now().isoformat("T")
        self.updated_at = datetime.now().isoformat("T")
        dct.update({'__class__': type(self).__name__})
        return dct
