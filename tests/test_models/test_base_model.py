#!/usr/bin/python3
""" Testing Base Class """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ For testing the BaseModel """

    def setUp(self):
        self.obj = BaseModel()

