#!/usr/bin/python3


from models.base_model import BaseModel
import uuid
import datetime
from time import sleep



import unittest

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.shared_model = BaseModel()
        self.shared_model.name = "My_First_Model"
        self.shared_model.my_number = 89

    def test_type(self):
        self.assertEqual(BaseModel, type(BaseModel()))
        self.assertEqual(BaseModel, type(self.shared_model))


    def test_NoneKwargs(self):
        expected_output = f"[BaseModel] ({self.shared_model.id}) {self.shared_model.__dict__}"
        actual_output = str(self.shared_model)
        expected_output_dict = {
            '__class__': 'BaseModel',
            'id': self.shared_model.id,
            'created_at': self.shared_model.created_at.isoformat(),
            'updated_at': self.shared_model.updated_at.isoformat(),
            'name': self.shared_model.name,
            'my_number': self.shared_model.my_number
        }
        actual_output_dict = self.shared_model.to_dict()

        self.assertIsInstance(self.shared_model.id, str)
        self.assertIsInstance(self.shared_model.created_at, datetime.datetime)
        self.assertIsInstance(self.shared_model.updated_at, datetime.datetime)
        self.assertIsInstance(self.shared_model.name, str)
        self.assertIsInstance(self.shared_model.my_number, int)
        self.assertEqual(actual_output, expected_output)
        self.assertDictEqual(actual_output_dict, expected_output_dict)

    def test_kwargs(self):
        mynew_model = BaseModel(**self.shared_model.to_dict())
        expected_output = f"[BaseModel] ({mynew_model.id}) {mynew_model.__dict__}"
        actual_output = str(mynew_model)
        expected_output_dict = {
            '__class__': 'BaseModel',
            'id': mynew_model.id,
            'created_at': mynew_model.created_at.isoformat(),
            'updated_at': mynew_model.updated_at.isoformat(),
            'name': mynew_model.name,
            'my_number': mynew_model.my_number
        }
        actual_output_dict = mynew_model.to_dict()

        self.assertIsInstance(mynew_model.id, str)
        self.assertIsInstance(mynew_model.created_at, datetime.datetime)
        self.assertIsInstance(mynew_model.updated_at, datetime.datetime)
        self.assertIsInstance(mynew_model.name, str)
        self.assertIsInstance(mynew_model.my_number, int)
        self.assertEqual(actual_output, expected_output)
        self.assertDictEqual(actual_output_dict, expected_output_dict)

    def test_time(self):
        sleep(0.05)
        new = BaseModel()
        self.assertNotEqual(new.created_at, self.shared_model.created_at)
        self.assertLess(self.shared_model.created_at, new.created_at)
        sleep(0.05)
        new.save()
        self.assertNotEqual(new.created_at, new.updated_at)
        self.assertLess(new.created_at, new.updated_at)




if __name__ == '__main__':
    unittest.main()
