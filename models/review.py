#!/usr/bin/python3
"""Review model."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class from BaseModel"""

    place_id = ''   # will be Place.id
    user_id = ''    # will be User.id
    test = ''
