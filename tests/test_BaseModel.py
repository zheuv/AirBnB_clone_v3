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
        expected_output_dict = {
            '__class__': 'BaseModel',
            'id': my_model.id,
            'created_at': my_model.created_at.isoformat(),
            'updated_at': my_model.updated_at.isoformat(),
            'name': my_model.name,
            'my_number': my_model.my_number
        }
        actual_output_dict = my_model.to_dict()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime.datetime)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)
        self.assertIsInstance(my_model.name, str)
        self.assertIsInstance(my_model.my_number, int)
        self.assertEqual(actual_output, expected_output)
        self.assertDictEqual(actual_output_dict, expected_output_dict)

if __name__ == '__main__':
    unittest.main()
