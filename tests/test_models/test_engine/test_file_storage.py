#!/usr/bin/python3

"""tests User"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """ test user model"""
    @classmethod
    def setUp(cls):
        """steup class method"""
        cls.storage = FileStorage()
        cls.my_module = BaseModel()

    def test_FileStorage_doc(self):
        """check if docstring for class is present"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_FileStorage_methods_doc(self):
        """docstring exist for all methods"""
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_FileStorageClass(self):
        """ check the type of instante"""
        self.assertIsInstance(self.storage, FileStorage)
        self.assertEqual(type(self.storage), FileStorage)

    def test_save(self):
        """test save"""
        self.storage.new(self.my_module)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        """test all"""
        dct = self.storage.all()
        self.assertIsInstance(dct, dict)

    def test_new(self):
        """ test new """
        key = "BaseModel" + "." + self.my_module.id
        self.storage.new(self.my_module)
        self.assertEqual(self.my_module, self.storage.all()[key])

    def test_realod(self):
        """ test realod"""
        self.assertFalse(self.storage.reload())
        os.remove("file.json")
        self.assertRaises(FileNotFoundError, self.storage.reload())

    @classmethod
    def tearDownClass(cls):
        """clear objects after all test"""
        del cls.storage
        del cls.my_module


if __name__ == '__main__':
    unittest.main()
