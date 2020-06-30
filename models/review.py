#!/usr/bin/python3
"""
python module
"""
from models.base_model import BaseModel
import models


class Review(BaseModel):
    """Class Review"""
    place_id = ""
    user_id = ""
    text = ""
