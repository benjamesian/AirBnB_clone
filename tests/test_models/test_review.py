import unittest
from models.review import Review


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
