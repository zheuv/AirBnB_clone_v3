#!/usr/bin/python3

from models.user import User
import uuid
import datetime
from time import sleep
import unittest

class TestUser(unittest.TestCase):
    def setUp(self):
        self.shared_user = User()
        self.shared_user.name = "My_First_User"
        self.shared_user.my_number = 89

    def test_type(self):
        self.assertEqual(User, type(User()))
        self.assertEqual(User, type(self.shared_user))
    
    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))
    def test_NoneKwargs(self):
        expected_output = f"[User] ({self.shared_user.id}) {self.shared_user.__dict__}"
        actual_output = str(self.shared_user)
        expected_output_dict = {
            '__class__': 'User',
            'id': self.shared_user.id,
            'created_at': self.shared_user.created_at.isoformat(),
            'updated_at': self.shared_user.updated_at.isoformat(),
            'name': self.shared_user.name,
            'my_number': self.shared_user.my_number
        }
        actual_output_dict = self.shared_user.to_dict()

        self.assertIsInstance(self.shared_user.id, str)
        self.assertIsInstance(self.shared_user.created_at, datetime.datetime)
        self.assertIsInstance(self.shared_user.updated_at, datetime.datetime)
        self.assertIsInstance(self.shared_user.name, str)
        self.assertIsInstance(self.shared_user.my_number, int)
        self.assertEqual(actual_output, expected_output)
        self.assertDictEqual(actual_output_dict, expected_output_dict)

    def test_kwargs(self):
        mynew_user = User(**self.shared_user.to_dict())
        expected_output = f"[User] ({mynew_user.id}) {mynew_user.__dict__}"
        actual_output = str(mynew_user)
        expected_output_dict = {
            '__class__': 'User',
            'id': mynew_user.id,
            'created_at': mynew_user.created_at.isoformat(),
            'updated_at': mynew_user.updated_at.isoformat(),
            'name': mynew_user.name,
            'my_number': mynew_user.my_number
        }
        actual_output_dict = mynew_user.to_dict()

        self.assertIsInstance(mynew_user.id, str)
        self.assertIsInstance(mynew_user.created_at, datetime.datetime)
        self.assertIsInstance(mynew_user.updated_at, datetime.datetime)
        self.assertIsInstance(mynew_user.name, str)
        self.assertIsInstance(mynew_user.my_number, int)
        self.assertEqual(actual_output, expected_output)
        self.assertDictEqual(actual_output_dict, expected_output_dict)

    def test_time(self):
        sleep(0.05)
        new = User()
        self.assertNotEqual(new.created_at, self.shared_user.created_at)
        self.assertLess(self.shared_user.created_at, new.created_at)
        sleep(0.05)
        new.save()
        self.assertNotEqual(new.created_at, new.updated_at)
        self.assertLess(new.created_at, new.updated_at)

if __name__ == '__main__':
    unittest.main()
