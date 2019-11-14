import unittest
from models.review import Review
import pep8


class TestState(unittest.TestCase):
    """testing inherited functionality from BaseModel"""

    def setUp(self):
        """test obj instantiation"""
        self.obj = Review()

    def test_Attrs(self):
        """checks the existence of expected attrs"""
        self.assertTrue(hasattr(self.obj, 'place_id'))
        self.assertTrue(hasattr(self.obj, 'user_id'))
        self.assertTrue(hasattr(self.obj, 'text'))

    def test_pep8_conformance(self):
        """test for pep8 conformance"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Found pep8 errors")
