#!/usr/bin/python3

from models.state import State
import uuid
import datetime
from time import sleep
import unittest

class TestState(unittest.TestCase):
    def setUp(self):
        self.shared_state = State()
        self.shared_state.name = "My_First_State"
        self.shared_state.my_number = 89

    def test_type(self):
        self.assertEqual(State, type(State()))
        self.assertEqual(State, type(self.shared_state))

    def test_NoneKwargs(self):
        expected_output = f"[State] ({self.shared_state.id}) {self.shared_state.__dict__}"
        actual_output = str(self.shared_state)
        expected_output_dict = {
            '__class__': 'State',
            'id': self.shared_state.id,
            'created_at': self.shared_state.created_at.isoformat(),
            'updated_at': self.shared_state.updated_at.isoformat(),
            'name': self.shared_state.name,
            'my_number': self.shared_state.my_number
        }
        actual_output_dict = self.shared_state.to_dict()

        self.assertIsInstance(self.shared_state.id, str)
        self.assertIsInstance(self.shared_state.created_at, datetime.datetime)
        self.assertIsInstance(self.shared_state.updated_at, datetime.datetime)
        self.assertIsInstance(self.shared_state.name, str)
        self.assertIsInstance(self.shared_state.my_number, int)
        self.assertEqual(actual_output, expected_output)
        self.assertDictEqual(actual_output_dict, expected_output_dict)

    def test_kwargs(self):
        mynew_state = State(**self.shared_state.to_dict())
        expected_output = f"[State] ({mynew_state.id}) {mynew_state.__dict__}"
        actual_output = str(mynew_state)
        expected_output_dict = {
            '__class__': 'State',
            'id': mynew_state.id,
            'created_at': mynew_state.created_at.isoformat(),
            'updated_at': mynew_state.updated_at.isoformat(),
            'name': mynew_state.name,
            'my_number': mynew_state.my_number
        }
        actual_output_dict = mynew_state.to_dict()

        self.assertIsInstance(mynew_state.id, str)
        self.assertIsInstance(mynew_state.created_at, datetime.datetime)
        self.assertIsInstance(mynew_state.updated_at, datetime.datetime)
        self.assertIsInstance(mynew_state.name, str)
        self.assertIsInstance(mynew_state.my_number, int)
        self.assertEqual(actual_output, expected_output)
        self.assertDictEqual(actual_output_dict, expected_output_dict)

    def test_time(self):
        sleep(0.05)
        new = State()
        self.assertNotEqual(new.created_at, self.shared_state.created_at)
        self.assertLess(self.shared_state.created_at, new.created_at)
        sleep(0.05)
        new.save()
        self.assertNotEqual(new.created_at, new.updated_at)
        self.assertLess(new.created_at, new.updated_at)

if __name__ == '__main__':
    unittest.main()
