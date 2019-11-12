#!/usr/bin/python3
"""Base class for all application objects"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """
    defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """initialization"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
            f = "%Y-%m-%dT%H:%M:%S.%f"
            self.created_at = datetime.strptime(self.created_at, f)
            self.updated_at = datetime.strptime(self.updated_at, f)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            models.storage.new(self)

    def __str__(self):
        """custom str"""
        return "[{:s}] ({:s}) {:s}"\
            .format(self.__class__.__name__, self.id, str(self.__dict__))

    def save(self):
        """
        updates `updated_at` with the current datetime
        stores savetime in storage
        """
        self.updated_at = datetime.now()

        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of instance __dict__
        """
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()

        return dic
