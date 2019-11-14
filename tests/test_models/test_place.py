import unittest
from models.place import Place
import pep8


class TestState(unittest.TestCase):
    """testing inherited functionality from BaseModel"""

    def setUp(self):
        """test obj instantiation"""
        self.obj = Place()

    def test_Attrs(self):
        """checks the existence of expected attrs"""
        self.assertTrue(hasattr(self.obj, 'city_id'))
        self.assertTrue(hasattr(self.obj, 'user_id'))
        self.assertTrue(hasattr(self.obj, 'name'))
        self.assertTrue(hasattr(self.obj, 'description'))
        self.assertTrue(hasattr(self.obj, 'number_rooms'))
        self.assertTrue(hasattr(self.obj, 'number_bathrooms'))
        self.assertTrue(hasattr(self.obj, 'max_guest'))
        self.assertTrue(hasattr(self.obj, 'price_by_night'))
        self.assertTrue(hasattr(self.obj, 'latitude'))
        self.assertTrue(hasattr(self.obj, 'longitude'))
        self.assertTrue(hasattr(self.obj, 'amenity_ids'))

    def test_pep8_conformance(self):
        """test for pep8 conformance"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "Found pep8 errors")
