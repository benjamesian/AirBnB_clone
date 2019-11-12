#!/usr/bin/python3
"""Unit Tests for Console"""
import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
import re


class TestConsole(unittest.TestCase):
    """ For testing the Console """

    def setUp(self):
        self.console = HBNBCommand()

    def test_quit(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd('quit')
        with self.assertRaises(SystemExit):
            self.console.onecmd('quit more words')

    def test_EOF(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd('EOF')

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create')
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create howdy')
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create BaseModel')
            reg = re.compile(
                '[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'
            )
            self.assertRegex(f.getvalue(), reg)
