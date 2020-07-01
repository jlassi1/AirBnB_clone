#!/usr/bin/python3

"""tests User"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestUser(unittest.TestCase):
    """ test user model"""
    @classmethod
    def setUp(cls):
        """steup class method"""
        cls.city = City()
        cls.city.name = "Betty"
        cls.city.state_id = "root"

    def test_name(self):
        """ test first name"""
        b = City()
        self.assertEqual(self.city.name, "Betty")
        self.assertIsInstance(self.city.name, str)
        self.assertEqual(b.name, "")

    def test_state_id(self):
        """ test last name"""
        b = City()
        self.assertEqual(self.city.state_id, "root")
        self.assertIsInstance(self.city.state_id, str)
        self.assertEqual(b.state_id, "")

    def test_CityClass(self):
        """ check the type of instante"""
        self.assertTrue(issubclass(City, BaseModel))
        self.assertIsInstance(self.city, City)
        self.assertIsNotNone(City.__doc__)

    @classmethod
    def tearDownClass(cls):
        """clear objects after all test"""
        del cls.city.name
        del cls.city.state_id
        del cls.city
