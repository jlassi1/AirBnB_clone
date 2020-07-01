#!/usr/bin/python3

"""tests Review"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ test Review model"""
    @classmethod
    def setUp(cls):
        """steup class method"""
        cls.Review = Review()
        cls.Review.user_id = "Betty"
        cls.Review.place_id = "Tunis"
        cls.Review.text = "holberton tunis"

    def test_user_id(self):
        """ test  user_id"""
        b = Review()
        self.assertEqual(self.Review.user_id, "Betty")
        self.assertIsInstance(self.Review.user_id, str)
        self.assertEqual(b.user_id, "")

    def test_place_id(self):
        """ test place id"""
        b = Review()
        self.assertEqual(self.Review.place_id, "Tunis")
        self.assertIsInstance(self.Review.place_id, str)
        self.assertEqual(b.place_id, "")

    def test_text(self):
        """ test text"""
        b = Review()
        self.assertEqual(self.Review.text, "holberton tunis")
        self.assertIsInstance(self.Review.text, str)
        self.assertEqual(b.text, "")

    def test_ReviewClass(self):
        """ check the type of instante"""
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertIsInstance(self.Review, Review)
        self.assertIsNotNone(Review.__doc__)

    @classmethod
    def tearDownClass(cls):
        """clear objects after all test"""
        del cls.Review.user_id
        del cls.Review.place_id
        del cls.Review


if __name__ == '__main__':
    unittest.main()
