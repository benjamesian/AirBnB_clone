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
        """create test obj"""
        self.console = HBNBCommand()

    def test_quit(self):
        """test quit functionality"""
        with self.assertRaises(SystemExit):
            self.console.onecmd('quit')
        with self.assertRaises(SystemExit):
            self.console.onecmd('quit more words')

    def test_EOF(self):
        """test eof signal"""
        with self.assertRaises(SystemExit):
            self.console.onecmd('EOF')

    def test_create(self):
        """test beneral"""
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

    def test_empty(self):
        """test empty string submission"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('')
            self.assertEqual(f.getvalue(), "")
        self.console.onecmd('all')
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('')
            self.assertEqual(f.getvalue(), "")

    def test_all(self):
        """test the all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('all FakeModel')
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_update(self):
        """test the update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('update')
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('update FakeModel')
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('update FakeModel')
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('update BaseModel')
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('update BaseModel FakeId')
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            instance_id = f.getvalue().rstrip('\n')
            with patch('sys.stdout', new=StringIO()) as g:
                self.console.onecmd(
                    'update BaseModel {:s}'.format(instance_id))
                self.assertEqual(
                    g.getvalue(), "** attribute name missing **\n")
            with patch('sys.stdout', new=StringIO()) as g:
                self.console.onecmd(
                    'update BaseModel {:s} hi'.format(instance_id))
                self.assertEqual(g.getvalue(), "** value missing **\n")
