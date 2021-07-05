#!/usr/bin/python3
"""test module for console.py"""

import os
import unittest
from models import storage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):
    """tests the HBNB command interpreter"""

    def test_emptyline(self):
        HBNBCommand().onecmd("")

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
            HBNBCommand().onecmd("create")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_create_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    """show command"""
    def test_show_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("show")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_show_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("show MyModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_show_missing_id(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_show_invalid_id(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("show BaseModel 121212")
            self.assertEqual(expected, obtained.getvalue().strip())

    """destroy command"""
    def test_destroy_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_destroy_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("destroy MyModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_destroy_missing_id(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_destroy_invalid_id(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("destroy BaseModel 121212")
            self.assertEqual(expected, obtained.getvalue().strip())

    """all command"""
    def test_all_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("all MyModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    """update command"""
    def test_update_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("update")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("update MyModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_missing_id(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_invalid_id(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("update BaseModel 121212")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_missing_attribute(self):
        expected = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create BaseModel")
            id = obtained.getvalue().strip()
            command = "update BaseModel {}".format(id)
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_missing_value(self):
        expected = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create BaseModel")
            id = obtained.getvalue().strip()
            command = "update BaseModel {} first_name".format(id)
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertEqual(expected, obtained.getvalue().strip())


class TestHBNBCommand_classes(unittest.TestCase):
    """tests the HBNB command interpreter using the classes"""

    def test_all(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create State")
            HBNBCommand().onecmd("create City")
            HBNBCommand().onecmd("create Amenity")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("create Review")
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("BaseModel.all()")
            self.assertIn("BaseModel", obtained.getvalue().strip())
            self.assertNotIn("User", obtained.getvalue().strip())
            self.assertNotIn("State", obtained.getvalue().strip())
            self.assertNotIn("City", obtained.getvalue().strip())
            self.assertNotIn("Amenity", obtained.getvalue().strip())
            self.assertNotIn("Place", obtained.getvalue().strip())
            self.assertNotIn("Review", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("User.all()")
            self.assertIn("User", obtained.getvalue().strip())
            self.assertNotIn("BaseModel", obtained.getvalue().strip())
            self.assertNotIn("State", obtained.getvalue().strip())
            self.assertNotIn("City", obtained.getvalue().strip())
            self.assertNotIn("Amenity", obtained.getvalue().strip())
            self.assertNotIn("Place", obtained.getvalue().strip())
            self.assertNotIn("Review", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("State.all()")
            self.assertIn("State", obtained.getvalue().strip())
            self.assertNotIn("BaseModel", obtained.getvalue().strip())
            self.assertNotIn("User", obtained.getvalue().strip())
            self.assertNotIn("City", obtained.getvalue().strip())
            self.assertNotIn("Amenity", obtained.getvalue().strip())
            self.assertNotIn("Place", obtained.getvalue().strip())
            self.assertNotIn("Review", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("City.all()")
            self.assertIn("City", obtained.getvalue().strip())
            self.assertNotIn("BaseModel", obtained.getvalue().strip())
            self.assertNotIn("User", obtained.getvalue().strip())
            self.assertNotIn("State", obtained.getvalue().strip())
            self.assertNotIn("Amenity", obtained.getvalue().strip())
            self.assertNotIn("Place", obtained.getvalue().strip())
            self.assertNotIn("Review", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("Amenity.all()")
            self.assertIn("Amenity", obtained.getvalue().strip())
            self.assertNotIn("BaseModel", obtained.getvalue().strip())
            self.assertNotIn("User", obtained.getvalue().strip())
            self.assertNotIn("State", obtained.getvalue().strip())
            self.assertNotIn("City", obtained.getvalue().strip())
            self.assertNotIn("Place", obtained.getvalue().strip())
            self.assertNotIn("Review", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("Place.all()")
            self.assertIn("Place", obtained.getvalue().strip())
            self.assertNotIn("BaseModel", obtained.getvalue().strip())
            self.assertNotIn("User", obtained.getvalue().strip())
            self.assertNotIn("State", obtained.getvalue().strip())
            self.assertNotIn("City", obtained.getvalue().strip())
            self.assertNotIn("Amenity", obtained.getvalue().strip())
            self.assertNotIn("Review", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("Review.all()")
            self.assertIn("Review", obtained.getvalue().strip())
            self.assertNotIn("BaseModel", obtained.getvalue().strip())
            self.assertNotIn("User", obtained.getvalue().strip())
            self.assertNotIn("State", obtained.getvalue().strip())
            self.assertNotIn("City", obtained.getvalue().strip())
            self.assertNotIn("Amenity", obtained.getvalue().strip())
            self.assertNotIn("Place", obtained.getvalue().strip())

    def test_count(self):
        os.remove("file.json")
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create State")
            HBNBCommand().onecmd("create City")
            HBNBCommand().onecmd("create City")
            HBNBCommand().onecmd("create Amenity")
            HBNBCommand().onecmd("create Place")
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual("4", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual("2", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("State.count()")
            self.assertEqual("2", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("City.count()")
            self.assertEqual("3", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual("2", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("Place.count()")
            self.assertEqual("2", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("Review.count()")
            self.assertEqual("1", obtained.getvalue().strip())

    def test_show(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create BaseModel")
            id = obtained.getvalue().strip()
            command = 'BaseModel.show("' + obtained.getvalue().strip() + '")'
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertIn(id, obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create User")
            id = obtained.getvalue().strip()
            command = 'User.show("' + obtained.getvalue().strip() + '")'
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertIn(id, obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create State")
            id = obtained.getvalue().strip()
            command = 'State.show("' + obtained.getvalue().strip() + '")'
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertIn(id, obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create City")
            id = obtained.getvalue().strip()
            command = 'City.show("' + obtained.getvalue().strip() + '")'
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertIn(id, obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Amenity")
            id = obtained.getvalue().strip()
            command = 'Amenity.show("' + obtained.getvalue().strip() + '")'
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertIn(id, obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Place")
            id = obtained.getvalue().strip()
            command = 'Place.show("' + obtained.getvalue().strip() + '")'
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertIn(id, obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Review")
            id = obtained.getvalue().strip()
            command = 'Review.show("' + obtained.getvalue().strip() + '")'
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertIn(id, obtained.getvalue().strip())

    def test_destroy(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create BaseModel")
            instance = 'BaseModel.' + obtained.getvalue().strip()
            command = 'BaseModel.destroy("{}")'.format(obtained.getvalue().strip())
            self.assertIn(instance, storage.all().keys())
            HBNBCommand().onecmd(command)
            self.assertNotIn(instance, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create User")
            instance = 'User.' + obtained.getvalue().strip()
            command = 'User.destroy("{}")'.format(obtained.getvalue().strip())
            self.assertIn(instance, storage.all().keys())
            HBNBCommand().onecmd(command)
            self.assertNotIn(instance, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create State")
            instance = 'State.' + obtained.getvalue().strip()
            command = 'State.destroy("{}")'.format(obtained.getvalue().strip())
            self.assertIn(instance, storage.all().keys())
            HBNBCommand().onecmd(command)
            self.assertNotIn(instance, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create City")
            instance = 'City.' + obtained.getvalue().strip()
            command = 'City.destroy("{}")'.format(obtained.getvalue().strip())
            self.assertIn(instance, storage.all().keys())
            HBNBCommand().onecmd(command)
            self.assertNotIn(instance, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Amenity")
            instance = 'Amenity.' + obtained.getvalue().strip()
            command = 'Amenity.destroy("{}")'.format(obtained.getvalue().strip())
            self.assertIn(instance, storage.all().keys())
            HBNBCommand().onecmd(command)
            self.assertNotIn(instance, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Place")
            instance = 'Place.' + obtained.getvalue().strip()
            command = 'Place.destroy("{}")'.format(obtained.getvalue().strip())
            self.assertIn(instance, storage.all().keys())
            HBNBCommand().onecmd(command)
            self.assertNotIn(instance, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Review")
            instance = 'Review.' + obtained.getvalue().strip()
            command = 'Review.destroy("{}")'.format(obtained.getvalue().strip())
            self.assertIn(instance, storage.all().keys())
            HBNBCommand().onecmd(command)
            self.assertNotIn(instance, storage.all().keys())


if __name__ == "__main__":
    unittest.main()
