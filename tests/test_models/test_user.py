#!/usr/bin/python3

"""tests User"""
import unittest
import uuid
from datetime import datetime
from models.user import User
import models


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

    def test_User_cls_doc(self):
        """check if docstring for class is present"""
        self.assertIsNotNone(User.__doc__)

    def test_User_methods_doc(self):
        """docstring exist for all methods"""
        self.assertIsNotNone(User.__init__.__doc__)
        self.assertIsNotNone(User.__str__.__doc__)
        self.assertIsNotNone(User.save.__doc__)
        self.assertIsNotNone(User.to_dict.__doc__)
        self.assertIsInstance(self.my_user.to_dict(), dict)

    def test_type(self):
        """ check the type of instante"""
        self.assertIsInstance(self.my_user.first_name, str)
        self.assertIsInstance(self.my_user.last_name, str)
        self.assertIsInstance(self.my_user.email, str)
        self.assertIsInstance(self.my_user.password, str)
        self.assertIsInstance(self.my_user.created_at, datetime)
        self.assertTrue(issubclass(User, models.base_model.BaseModel))

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


if __name__ == '__main__':
    unittest.main()
