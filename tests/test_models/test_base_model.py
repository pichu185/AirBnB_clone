#!/usr/bin/python3
"""test module for class BaseModel"""

import models
import datetime
import unittest


class BaseModelTest(unittest.TestCase):
    """tests the class BaseModel"""

    def test_documentation(self):
        """tests module, class and methods docstring"""
        self.assertIsNotNone(models.base_model.__doc__)
        self.assertIsNotNone(models.base_model.BaseModel.__doc__)
        self.assertIsNotNone(models.base_model.BaseModel.__str__.__doc__)
        self.assertIsNotNone(models.base_model.BaseModel.save.__doc__)
        self.assertIsNotNone(models.base_model.BaseModel.to_dict.__doc__)

    def test_class(self):
        """test instance class"""
        instance = models.base_model.BaseModel()
        self.assertIsInstance(instance, models.base_model.BaseModel)

    def test_type(self):
        """test type of instance atributes"""
        instance = models.base_model.BaseModel()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
