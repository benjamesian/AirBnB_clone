#!/usr/bin/python3
""" Testing File Storage """
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
from os import path
import json
import pep8


class TestFileStorage(unittest.TestCase):
    """Class for testing FileStorage objects"""

    def setUp(self):
        """Create FileStorage object."""
        self.fs = FileStorage()

    def test_file(self):
        """checks if file exists"""
        self.assertTrue(isinstance(self.fs._FileStorage__file_path, str))

    def test_objects(self):
        """testing if __objects exists"""
        self.assertTrue(isinstance(self.fs._FileStorage__objects, dict))

    def test_all(self):
        """Test all method."""
        self.assertIsInstance(self.fs.all(), dict)

    def test_new(self):
        """Test new method."""
        b = BaseModel()
        self.fs.new(b)
        key = b.__class__.__name__ + '.' + str(b.id)
        self.assertIn(key, self.fs.all())

    def test_save(self):
        """Test save method."""
        c = BaseModel()
        key = c.__class__.__name__ + '.' + str(c.id)
        self.fs.save()
        filename = 'file.json'
        self.assertTrue(path.isfile(filename))
        with open(filename, 'r') as f:
            dic = json.load(f)
        self.assertIn(key, dic.keys())

    def test_reload(self):
        """Test reload method."""
        self.fs.reload()
        self.assertIsInstance(self.fs.all(), dict)

        filename = 'file.json'
        if (path.isfile(filename)):
            with open(filename, 'r') as f:
                with open('file_copy', 'w') as g:
                    g.write(f.read())
            os.remove(filename)
            try:
                self.fs.reload()
            except Exception as e:
                self.fail('reload raised exception when no file: {}'.format(e))
            with open('file_copy', 'r') as f:
                with open(filename, 'w') as g:
                    g.write(f.read())
            os.remove('file_copy')
        else:
            try:
                self.fs.reload()
            except Exception as e:
                self.fail('reload raised exception when no file: {}'.format(e))

    def test_pep8_conformance(self):
        """test for pep8 conformance"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Found pep8 errors")
