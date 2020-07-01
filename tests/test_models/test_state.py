#!/usr/bin/python3

"""tests User"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestUser(unittest.TestCase):
    """ test user model"""
    @classmethod
    def setUp(cls):
        """steup class method"""
        cls.State = State()
        cls.State.name = "Betty"

    def test_name(self):
        """ test name"""
        b = State()
        self.assertEqual(self.State.name, "Betty")
        self.assertIsInstance(self.State.name, str)
        self.assertEqual(b.name, "")

    def test_StateClass(self):
        """ check the type of instante"""
        self.assertTrue(issubclass(State, BaseModel))
        self.assertIsInstance(self.State, State)
        self.assertIsNotNone(State.__doc__)

    @classmethod
    def tearDownClass(cls):
        """clear objects after all test"""
        del cls.State.name
        del cls.State


if __name__ == '__main__':
    unittest.main()