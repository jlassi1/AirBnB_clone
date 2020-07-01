#!/usr/bin/python3

"""tests User"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestUser(unittest.TestCase):
    """ test user model"""
    @classmethod
    def setUp(cls):
        """steup class method"""
        cls.Amenity = Amenity()
        cls.Amenity.name = "Betty"

    def test_name(self):
        """ test name"""
        b = Amenity()
        self.assertEqual(self.Amenity.name, "Betty")
        self.assertIsInstance(self.Amenity.name, str)
        self.assertEqual(b.name, "")

    def test_AmenityClass(self):
        """ check the type of instante"""
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertIsInstance(self.Amenity, Amenity)
        self.assertIsNotNone(Amenity.__doc__)

    @classmethod
    def tearDownClass(cls):
        """clear objects after all test"""
        del cls.Amenity.name
        del cls.Amenity


if __name__ == '__main__':
    unittest.main()