#!/usr/bin/python3
"""
python module
"""
from models.base_model import BaseModel
import uuid
from datetime import datetime
import models


class City(BaseModel):
    """Class City"""
    state_id = ""
    name = ""
