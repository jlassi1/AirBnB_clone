#!/usr/bin/python3

"""tests User"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage
import pep8
import os


class TestUser(unittest.TestCase):
    """ test user model"""
    @classmethod
    def setUp(cls):
        """steup class method"""
        cls.my_user = User()
        cls.my_user.first_name = "Betty"
        cls.my_user.last_name = "Holberton"
        cls.my_user.email = "airbnb@holbertonshool.com"
        cls.my_user.password = "root"
        cls.my_user.save()

    def test_email(self):
        """test email"""
        self.assertNotEqual(self.my_user.email, "mbmb@holbertonshool.com")
        self.assertTrue(self.my_user.email, "airbnb@holbertonshool.com")
        self.assertIsInstance(self.my_user.email, str)

    def test_first_name(self):
        """ test first name"""
        b = User()
        self.assertEqual(self.my_user.first_name, "Betty")
        self.assertIsInstance(self.my_user.first_name, str)
        self.assertEqual(b.first_name, "")

    def test_last_name(self):
        """ test last name"""
        b = User()
        self.assertEqual(self.my_user.password, "root")
        self.assertIsInstance(self.my_user.password, str)
        self.assertEqual(b.password, "")

    def test_password(self):
        """ test password"""
        b = User()
        self.assertEqual(self.my_user.last_name, "Holberton")
        self.assertIsInstance(self.my_user.last_name, str)
        self.assertEqual(b.last_name, "")

    def test_save(self):
        """test save"""
        b = User()
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)

    def test_type(self):
        """ check the type of instante"""
        self.assertIsInstance(self.my_user.first_name, str)
        self.assertIsInstance(self.my_user.last_name, str)
        self.assertIsInstance(self.my_user.email, str)
        self.assertIsInstance(self.my_user.password, str)
        self.assertIsInstance(self.my_user.created_at, datetime)
        self.assertTrue(issubclass(User, BaseModel))

    def test_User_instant(self):
        """ """
        usr = self.my_user
        self.assertEqual(self.my_user.created_at, usr.created_at)
        self.assertEqual(self.my_user.updated_at, usr.updated_at)
        self.assertEqual(self.my_user.first_name, usr.first_name)
        self.assertEqual(self.my_user.last_name, usr.last_name)
        self.assertEqual(self.my_user.email, usr.email)
        self.assertEqual(self.my_user.password, usr.password)
        self.assertDictEqual(self.my_user.to_dict(), usr.to_dict())
        self.assertAlmostEqual(self.my_user.to_dict(), usr.to_dict())

    @classmethod
    def tearDownClass(cls):
        """clear objects after all test"""
        del cls.my_user.first_name
        del cls.my_user.last_name
        del cls.my_user.email
        del cls.my_user.password
        del cls.my_user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
