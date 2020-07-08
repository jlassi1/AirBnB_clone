#!/usr/bin/python3

"""tests place"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.user import User


class TestPlace(unittest.TestCase):
    """ test Place model"""
    @classmethod
    def setUp(cls):
        """steup class method"""
        cls.c = City()
        cls.u = User()
        cls.my_Place = Place()
        cls.my_Place.city_id = cls.c.id
        cls.my_Place.user_id = cls.u.id
        cls.my_Place.description = "Nice"
        cls.my_Place.number_bathrooms = 3
        cls.my_Place.max_guest = 5
        cls.my_Place.price_by_night = 7
        cls.my_Place.latitude = 4.5
        cls.my_Place.longitude = 8.3
        cls.my_Place.name = "Betty"
        cls.my_Place.amenity_ids = Amenity().id

    def test_name(self):
        """ test name"""
        b = Place()
        self.assertEqual(self.my_Place.name, Amenity.id)
        self.assertIsInstance(self.my_Place.name, str)
        self.assertEqual(b.name, "")

    def test_longitude(self):
        """ test longitude"""
        b = Place()
        self.assertEqual(self.my_Place.longitude, 8.3)
        self.assertIsInstance(self.my_Place.longitude, float)
        self.assertEqual(b.longitude, 0)

    def test_latitude(self):
        """ test latitude"""
        b = Place()
        self.assertEqual(self.my_Place.latitude, 4.5)
        self.assertIsInstance(self.my_Place.latitude, float)
        self.assertEqual(b.latitude, 0)

    def test_price_by_night(self):
        """ test price_by_night"""
        b = Place()
        self.assertEqual(self.my_Place.price_by_night, 7)
        self.assertIsInstance(self.my_Place.price_by_night, int)
        self.assertEqual(b.price_by_night, 0)

    def test_max_guest(self):
        """ test max_guest"""
        b = Place()
        self.assertEqual(self.my_Place.max_guest, 5)
        self.assertIsInstance(self.my_Place.max_guest, int)
        self.assertEqual(b.max_guest, 0)

    def test_name(self):
        """ test name"""
        b = Place()
        self.assertEqual(self.my_Place.name, "Betty")
        self.assertIsInstance(self.my_Place.name, str)
        self.assertEqual(b.name, "")

    def test_description(self):
        """test description"""
        b = Place()
        self.assertNotEqual(self.my_Place.description, "NIce")
        self.assertTrue(self.my_Place.description, "Nice")
        self.assertIsInstance(self.my_Place.description, str)
        self.assertEqual(b.description, "")

    def test_city_id(self):
        """ test city id"""
        b = Place()
        self.assertEqual(self.my_Place.city_id, self.c.id)
        self.assertIsInstance(self.my_Place.city_id, str)
        self.assertEqual(b.city_id, "")

    def test_number_bathrooms(self):
        """ test number_bathrooms"""
        b = Place()
        self.assertEqual(self.my_Place.number_bathrooms, 3)
        self.assertIsInstance(self.my_Place.number_bathrooms, int)
        self.assertEqual(b.number_bathrooms, 0)

    def test_user_id(self):
        """ test user id"""
        b = Place()
        self.assertEqual(self.my_Place.user_id, self.u.id)
        self.assertIsInstance(self.my_Place.user_id, str)
        self.assertEqual(b.user_id, "")

    def test_PlaceClass(self):
        """ check the type of instante"""
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertIsInstance(self.my_Place, Place)

    def test_Place_instant(self):
        """ """
        ps = self.my_Place
        self.assertEqual(self.my_Place.price_by_night, ps.price_by_night)
        self.assertEqual(self.my_Place.max_guest, ps.max_guest)
        self.assertEqual(self.my_Place.city_id, ps.city_id)
        self.assertEqual(self.my_Place.user_id, ps.user_id)
        self.assertEqual(self.my_Place.description, ps.description)
        self.assertEqual(self.my_Place.number_bathrooms, ps.number_bathrooms)
        self.assertDictEqual(self.my_Place.to_dict(), ps.to_dict())
        self.assertAlmostEqual(self.my_Place.to_dict(), ps.to_dict())

    @classmethod
    def tearDownClass(cls):
        """clear objects after all test"""
        del cls.my_Place.city_id
        del cls.my_Place.user_id
        del cls.my_Place.description
        del cls.my_Place.number_bathrooms
        del cls.my_Place.max_guest
        del cls.my_Place.price_by_night
        del cls.my_Place.latitude
        del cls.my_Place.longitude
        del cls.my_Place.amenity_ids
        del cls.my_Place.name
        del cls.c
        del cls.u
        del cls.my_Place


if __name__ == '__main__':
    unittest.main()
