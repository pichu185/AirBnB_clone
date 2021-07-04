#!/usr/bin/python3
"""test module for console.py"""

import unittest
from models import storage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):
    """tests the HBNB command interpreter"""

    def test_emptyline(self):
        self.assertFalse(HBNBCommand().onecmd(""))

    def test_do_quit(self):
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_do_EOF(self):
        self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_errors(unittest.TestCase):
    """tests the HBNB command interpreter"""

    """create command"""
    def test_create_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_create_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(expected, obtained.getvalue().strip())

    """show command"""
    def test_show_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_show_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_show_missing_id(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_show_invalid_id(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 121212"))
            self.assertEqual(expected, obtained.getvalue().strip())

    """destroy command"""
    def test_destroy_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_destroy_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_destroy_missing_id(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_destroy_invalid_id(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 121212"))
            self.assertEqual(expected, obtained.getvalue().strip())

    """all command"""
    def test_all_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(expected, obtained.getvalue().strip())

    """update command"""
    def test_update_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_missing_id(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_invalid_id(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 121212"))
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_missing_attribute(self):
        expected = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            id = obtained.getvalue().strip()
            command = "update BaseModel {}".format(id)
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_missing_value(self):
        expected = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            id = obtained.getvalue().strip()
            command = "update BaseModel {} first_name".format(id)
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(expected, obtained.getvalue().strip())


class TestHBNBCommand_BaseModel(unittest.TestCase):
    """tests the HBNB command interpreter using the 'BaseModel' class"""

    def test_create_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(obtained.getvalue().strip()))
            instance = "BaseModel." + obtained.getvalue().strip()
            self.assertIn(instance, storage.all().keys())


if __name__ == "__main__":
    unittest.main()
