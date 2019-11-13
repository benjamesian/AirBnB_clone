#!/usr/bin/python3

"""
Testing BaseModel
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Class testing the BaseModel """

    def setUp(self):
        self.obj = BaseModel()

    def test_init(self):
        """Test that attributes are initialized"""
        self.assertIsInstance(self.obj, BaseModel)
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    def test_instance(self):
        self.b = BaseModel()

    def test_id(self):
        """test id type"""
        self.assertIsInstance(self.obj.id, str)

    def test_datetime(self):
        """test if timestamps are datetimes"""
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_uuid(self):
        """Test that ids are unique"""
        other = BaseModel()
        self.assertNotEqual(self.obj.id, other.id)

    def test__str__(self):
        """test conversion to string of object"""
        self.assertIsInstance(str(self.obj), str)

    def test_to_dict(self):
        """test dictionary repr of BaseModels"""
        d = self.obj.to_dict()
        self.assertIsInstance(d, dict)
        self.assertTrue('__class__' in d)
        self.assertTrue('created_at' in d)
        self.assertTrue('updated_at' in d)
        f = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertIsInstance(datetime.strptime(d['created_at'], f), datetime)
        self.assertIsInstance(datetime.strptime(d['updated_at'], f), datetime)

    def test_init_kwargs(self):
        """ test updates to BaseModel using kwargs """
        kwargs_obj = BaseModel()
        dic = kwargs_obj.to_dict()
        new = BaseModel(**dic)

        self.assertEqual(new.id, kwargs_obj.id)
        self.assertEqual(new.__class__.__name__, kwargs_obj.__class__.__name__)

    def test_save(self):
        """ test save datetime obj """
        sobj = BaseModel()
        self.assertEqual(sobj.updated_at, sobj.created_at)

        sobj.save()
        self.assertEqual(type(sobj.updated_at), datetime)
        self.assertNotEqual(sobj.updated_at, sobj.created_at)
