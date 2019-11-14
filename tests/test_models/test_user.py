#!/usr/bin/python3
import unittest
from models.user import User
import pep8


class TestState(unittest.TestCase):
    """testing inherited functionality from BaseModel"""

    def setUp(self):
        """test obj instantiation"""
        self.obj = User()

    def test_Attrs(self):
        """checks the existence of expected attrs"""
        self.assertTrue(hasattr(self.obj, 'email'))
        self.assertTrue(hasattr(self.obj, 'password'))
        self.assertTrue(hasattr(self.obj, 'first_name'))
        self.assertTrue(hasattr(self.obj, 'last_name'))

    def test_pep8_conformance(self):
        """test for pep8 conformance"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "Found pep8 errors")
