#!/usr/bin/python3
"""test module for class FileStorage"""

import models
import datetime
import unittest


class FileStorageTest(unittest.TestCase):
    """tests the class FileStorage"""

    def test_documentation(self):
        """tests module, class and methods docstring"""
        self.assertIsNotNone(models.engine.file_storage.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.__doc__)
        shortcut = models.engine.file_storage.FileStorage
        self.assertIsNotNone(shortcut.__init__.__doc__)
        self.assertIsNotNone(shortcut.all.__doc__)
        self.assertIsNotNone(shortcut.new.__doc__)
        self.assertIsNotNone(shortcut.save.__doc__)
        self.assertIsNotNone(shortcut.reload.__doc__)
    def test_class(self):
        """test instance class"""
        instance = models.engine.file_storage.FileStorage()
        self.assertIsInstance(instance, models.engine.file_storage.FileStorage)


if __name__ == "__main__":
    unittest.main()
