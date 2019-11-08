#!/usr/bin/python3
""" Testing File Storage """
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
from os import path
import json

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.fs = FileStorage()

    def test_all(self):
        self.assertIsInstance(self.fs.all(), dict)

    def test_new(self):
        b = BaseModel()
        self.fs.new(b)
        key = b.__class__.__name__ + '.' + str(b.id)
        self.assertIsInstance(self.fs.all()[key], BaseModel)

    def test_save(self):
        self.fs.save()
        filename = 'file.JSON'
        self.assertTrue(path.isfile(filename))
        with open(filename, 'r') as f:
            self.assertIsInstance(json.load(f), dict)

    def test_reload(self):
        self.fs.reload()
        self.assertIsInstance(self.fs.all(), dict)

        filename = 'file.JSON'
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
