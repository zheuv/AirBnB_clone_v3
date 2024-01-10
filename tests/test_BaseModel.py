#!/usr/bin/python3


from models.base_model import BaseModel
import uuid
import datetime



import unittest

class TestBaseModel(unittest.TestCase):
    def test_NoneKwargs(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        expected_output = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        actual_output = str(my_model)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime.datetime)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)
        self.assertIsInstance(my_model.name, str)
        self.assertIsInstance(my_model.my_number, int)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
