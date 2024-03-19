#!/usr/bin/python3


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_constructor(self):
        """Test the constructor of BaseModel"""
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_str_method(self):
        """Test the __str__ method of BaseModel"""
        model = BaseModel()
        model_str = str(model)
        expected_str = f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}"
        self.assertEqual(model_str, expected_str)

    def test_save_method(self):
        """Test the save method of BaseModel"""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of BaseModel"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], model.__class__.__name__)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        """Add more assertions based on the expected structure of the dictionary"""

if __name__ == '__main__':
    unittest.main()
