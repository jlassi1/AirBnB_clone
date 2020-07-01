#!/usr/bin/python
"""
test module
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage
import pep8
import os


class TestUser(unittest.TestCase):
    """test User Class"""

    def setUp(self):
        """Setup Method
        Args:
            na
        Description:
            method will run before all test methods
        Return:
            na
        """

        self.a = User()
        self.a.email = "Heindrick@gmail.com"
        self.a.password = "Holberton"
        self.a.first_name = "Heiny"
        self.a.last_name = "Cheung"
        self.b = User()

    def tearDown(self):
        """teardown method
        Args:
            na
        Description:
            remove testing instances and delete file.json file
        Return:
            na
        """

        del self.a
        del self.b
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_conformance(self):
        """Test that we conform to PEP8"""

        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")

    def test_email(self):
        """Setup Method
        Args:
            na
        Description:
            test string id of instance
        Return:
            na
        """

        self.assertNotEqual(self.a.email, "HC@gmail.com")
        self.assertTrue(self.a.email, "Heindrick@gmail.com")
        self.assertIsInstance(self.a.email, str)
        self.assertIsInstance(self.b.email, str)

    def test_password(self):
        """Setup Method
        Args:
            na
        Description:
            test string id of instance
        Return:
            na
        """

        self.assertEqual(type(self.b.password), str)
        self.assertIsNotNone(self.a.password)
        self.assertIsNotNone(self.b.password)
        self.assertEqual(self.a.password, "Holberton")

    def test_first_name(self):
        """Setup Method
        Args:
            na
        Description:
            test string id of instance
        Return:
            na
        """

        self.assertEqual(self.a.first_name, "Heiny")
        self.assertIsInstance(self.b.first_name, str)
        self.assertIsInstance(self.b.first_name, str)
        self.assertEqual(self.b.first_name, "")

    def test_last_name(self):
        """Setup Method
        Args:
            na
        Description:
            test string id of instance
        Return:
            na
        """

        self.assertEqual(self.a.last_name, "Cheung")
        self.assertIsInstance(self.a.last_name, str)
        self.assertIsInstance(self.b.last_name, str)
        self.assertEqual(self.b.last_name, "")

    def test_inherit(self):
        """test method
        Args:
            na
        Description:
            if subclass of BaseModel
        Return:
            na
        """

        self.assertTrue(issubclass(User, BaseModel))

    def test_save(self):
        """test save"""

        self.b.save()
        self.assertNotEqual(self.b.created_at, self.b.updated_at)


if __name__ == "__main__":
    unittest.main()
