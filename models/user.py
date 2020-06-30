"""
"""
from models.base_model import BaseModel
import uuid
from datetime import datetime
import models


class User(BaseModel):
    """ """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    