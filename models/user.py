#!/usr/bin/python3
"""
python module
"""
from models.base_model import BaseModel
import uuid
from datetime import datetime
import models


class User(BaseModel):
    """Class User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    