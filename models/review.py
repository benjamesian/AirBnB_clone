#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class from BaseModel"""

    place_id = ''   # will be Place.id
    user_id = ''    # will be User.id
    test = ''
