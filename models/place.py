#!/usr/bin/python3
from models.base_model import BaseModel

class Place(BaseModel):
    """Place class from BaseModel"""

    city_id = ''# it will be the City.id
    user_id = ''# it will be the User.id
    name = ''
    description = ''
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guest = int(0)
    price_by_night = int(0)
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = []# it will be the list of Amenity.id later
