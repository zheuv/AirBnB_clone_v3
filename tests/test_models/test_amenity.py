#!/usr/bin/python3

from models.amenity import Amenity
import uuid
import datetime
from time import sleep
import unittest

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.shared_amenity = Amenity()
        self.shared_amenity.name = "My_First_Amenity"
        self.shared_amenity.my_number = 89

    def test_type(self):
        self.assertEqual(Amenity, type(Amenity()))
        self.assertEqual(Amenity, type(self.shared_amenity))

    def test_NoneKwargs(self):
        expected_output = f"[Amenity] ({self.shared_amenity.id}) {self.shared_amenity.__dict__}"
        actual_output = str(self.shared_amenity)
        expected_output_dict = {
            '__class__': 'Amenity',
            'id': self.shared_amenity.id,
            'created_at': self.shared_amenity.created_at.isoformat(),
            'updated_at': self.shared_amenity.updated_at.isoformat(),
            'name': self.shared_amenity.name,
            'my_number': self.shared_amenity.my_number
        }
        actual_output_dict = self.shared_amenity.to_dict()

        self.assertIsInstance(self.shared_amenity.id, str)
        self.assertIsInstance(self.shared_amenity.created_at, datetime.datetime)
        self.assertIsInstance(self.shared_amenity.updated_at, datetime.datetime)
        self.assertIsInstance(self.shared_amenity.name, str)
        self.assertIsInstance(self.shared_amenity.my_number, int)
        self.assertEqual(actual_output, expected_output)
        self.assertDictEqual(actual_output_dict, expected_output_dict)

    def test_kwargs(self):
        mynew_amenity = Amenity(**self.shared_amenity.to_dict())
        expected_output = f"[Amenity] ({mynew_amenity.id}) {mynew_amenity.__dict__}"
        actual_output = str(mynew_amenity)
        expected_output_dict = {
            '__class__': 'Amenity',
            'id': mynew_amenity.id,
            'created_at': mynew_amenity.created_at.isoformat(),
            'updated_at': mynew_amenity.updated_at.isoformat(),
            'name': mynew_amenity.name,
            'my_number': mynew_amenity.my_number
        }
        actual_output_dict = mynew_amenity.to_dict()

        self.assertIsInstance(mynew_amenity.id, str)
        self.assertIsInstance(mynew_amenity.created_at, datetime.datetime)
        self.assertIsInstance(mynew_amenity.updated_at, datetime.datetime)
        self.assertIsInstance(mynew_amenity.name, str)
        self.assertIsInstance(mynew_amenity.my_number, int)
        self.assertEqual(actual_output, expected_output)
        self.assertDictEqual(actual_output_dict, expected_output_dict)

    def test_time(self):
        sleep(0.05)
        new = Amenity()
        self.assertNotEqual(new.created_at, self.shared_amenity.created_at)
        self.assertLess(self.shared_amenity.created_at, new.created_at)
        sleep(0.05)
        new.save()
        self.assertNotEqual(new.created_at, new.updated_at)
        self.assertLess(new.created_at, new.updated_at)

if __name__ == '__main__':
    unittest.main()
