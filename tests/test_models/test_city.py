#!/usr/bin/python3

from models.place import Place
import uuid
import datetime
from time import sleep
import unittest

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.shared_place = Place()
        self.shared_place.name = "My_First_Place"
        self.shared_place.my_number = 89

    def test_type(self):
        self.assertEqual(Place, type(Place()))
        self.assertEqual(Place, type(self.shared_place))

    def test_NoneKwargs(self):
        expected_output = f"[Place] ({self.shared_place.id}) {self.shared_place.__dict__}"
        actual_output = str(self.shared_place)
        expected_output_dict = {
            '__class__': 'Place',
            'id': self.shared_place.id,
            'created_at': self.shared_place.created_at.isoformat(),
            'updated_at': self.shared_place.updated_at.isoformat(),
            'name': self.shared_place.name,
            'my_number': self.shared_place.my_number
        }
        actual_output_dict = self.shared_place.to_dict()

        self.assertIsInstance(self.shared_place.id, str)
        self.assertIsInstance(self.shared_place.created_at, datetime.datetime)
        self.assertIsInstance(self.shared_place.updated_at, datetime.datetime)
        self.assertIsInstance(self.shared_place.name, str)
        self.assertIsInstance(self.shared_place.my_number, int)
        self.assertEqual(actual_output, expected_output)
        self.assertDictEqual(actual_output_dict, expected_output_dict)

    def test_kwargs(self):
        mynew_place = Place(**self.shared_place.to_dict())
        expected_output = f"[Place] ({mynew_place.id}) {mynew_place.__dict__}"
        actual_output = str(mynew_place)
        expected_output_dict = {
            '__class__': 'Place',
            'id': mynew_place.id,
            'created_at': mynew_place.created_at.isoformat(),
            'updated_at': mynew_place.updated_at.isoformat(),
            'name': mynew_place.name,
            'my_number': mynew_place.my_number
        }
        actual_output_dict = mynew_place.to_dict()

        self.assertIsInstance(mynew_place.id, str)
        self.assertIsInstance(mynew_place.created_at, datetime.datetime)
        self.assertIsInstance(mynew_place.updated_at, datetime.datetime)
        self.assertIsInstance(mynew_place.name, str)
        self.assertIsInstance(mynew_place.my_number, int)
        self.assertEqual(actual_output, expected_output)
        self.assertDictEqual(actual_output_dict, expected_output_dict)

    def test_time(self):
        sleep(0.05)
        new = Place()
        self.assertNotEqual(new.created_at, self.shared_place.created_at)
        self.assertLess(self.shared_place.created_at, new.created_at)
        sleep(0.05)
        new.save()
        self.assertNotEqual(new.created_at, new.updated_at)
        self.assertLess(new.created_at, new.updated_at)

if __name__ == '__main__':
    unittest.main()
