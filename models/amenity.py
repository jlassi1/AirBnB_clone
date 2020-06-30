#!/usr/bin/python3
"""
python module
"""
from models.base_model import BaseModel
import uuid
from datetime import datetime
import models


class Amenity(BaseModel):
    """Class Amenity"""
    name = ""
