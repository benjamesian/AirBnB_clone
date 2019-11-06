#!/usr/bin/python3
""" Testing Base Class """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ For testing the BaseModel """


    def setUp(self):
        self.obj = BaseModel()

    def test_init(self):
        """ Test that attributes are initialized """
        self.assertIsInstance(self.obj, BaseModel)
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_uuid(self):
        """ Test that ids are unique """
        other = BaseModel()
        self.assertNotEqual(self.obj.id, other.id)

    def test_str(self):
        """ test conversion to string of object """
        self.assertIsInstance(str(self.obj), str)

    def test_to_dict(self):
        """ test dictionary repr of BaseModels """
        d = self.obj.to_dict()
        self.assertIsInstance(d, dict)
        self.assertTrue(hasattr(d, self.obj.__class__.__name__))
        self.assertTrue(hasattr(d, 'created_at'))
        self.assertTrue(hasattr(d, 'updated_at'))
        self.assertIsInstance(datetime.fromisoformat(d['created_at']), datetime)
        self.assertIsInstance(datetime.fromisoformat(d['updated_at']), datetime)
