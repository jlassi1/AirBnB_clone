"""tests basemodel"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ test base model"""
    @classmethod
    def setUp(cls):
        """steup class method"""
        cls.my_model = BaseModel()
        cls.my_model.name = "Holberton"
        cls.my_model.my_number = 89
        cls.my_model_json = cls.my_model.to_dict()
        cls.my_new_model = BaseModel(**cls.my_model_json)

    def test_BaseModel_cls_doc(self):
        """check if docstring for class is present"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_BaseModel_methods_doc(self):
        """docstring exist for all methods"""
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_type(self):
        """ check the type of instante"""
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.name, str)
        self.assertIsInstance(self.my_model.my_number, int)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertEqual(type(self.my_new_model.created_at), datetime)

    def test_BaseModel_methods(self):
        """ check the methods in class"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_BaseModel_instant(self):
        """ """
        bm = self.my_model
        self.assertEqual(self.my_model.created_at, bm.created_at)
        self.assertEqual(self.my_model.updated_at, bm.updated_at)
        self.assertEqual(self.my_model.id, bm.id)
        self.assertDictEqual(self.my_model.to_dict(), bm.to_dict())
        self.assertAlmostEqual(self.my_model.to_dict(), bm.to_dict())

    @classmethod
    def tearDownClass(cls):
        """clear objects after all test"""
        del cls.my_model.name
        del cls.my_model.my_number
        del cls.my_model_json
        del cls.my_new_model
        del cls.my_model


if __name__ == '__main__':
    unittest.main()
