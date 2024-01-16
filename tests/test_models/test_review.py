#!/usr/bin/python3

from models.review import Review
import uuid
import datetime
from time import sleep
import unittest

class TestReview(unittest.TestCase):
    def setUp(self):
        self.shared_review = Review()
        self.shared_review.name = "My_First_Review"
        self.shared_review.my_number = 89

    def test_type(self):
        self.assertEqual(Review, type(Review()))
        self.assertEqual(Review, type(self.shared_review))

    def test_NoneKwargs(self):
        expected_output = f"[Review] ({self.shared_review.id}) {self.shared_review.__dict__}"
        actual_output = str(self.shared_review)
        expected_output_dict = {
            '__class__': 'Review',
            'id': self.shared_review.id,
            'created_at': self.shared_review.created_at.isoformat(),
            'updated_at': self.shared_review.updated_at.isoformat(),
            'name': self.shared_review.name,
            'my_number': self.shared_review.my_number
        }
        actual_output_dict = self.shared_review.to_dict()

        self.assertIsInstance(self.shared_review.id, str)
        self.assertIsInstance(self.shared_review.created_at, datetime.datetime)
        self.assertIsInstance(self.shared_review.updated_at, datetime.datetime)
        self.assertIsInstance(self.shared_review.name, str)
        self.assertIsInstance(self.shared_review.my_number, int)
        self.assertEqual(actual_output, expected_output)
        self.assertDictEqual(actual_output_dict, expected_output_dict)

    def test_kwargs(self):
        mynew_review = Review(**self.shared_review.to_dict())
        expected_output = f"[Review] ({mynew_review.id}) {mynew_review.__dict__}"
        actual_output = str(mynew_review)
        expected_output_dict = {
            '__class__': 'Review',
            'id': mynew_review.id,
            'created_at': mynew_review.created_at.isoformat(),
            'updated_at': mynew_review.updated_at.isoformat(),
            'name': mynew_review.name,
            'my_number': mynew_review.my_number
        }
        actual_output_dict = mynew_review.to_dict()

        self.assertIsInstance(mynew_review.id, str)
        self.assertIsInstance(mynew_review.created_at, datetime.datetime)
        self.assertIsInstance(mynew_review.updated_at, datetime.datetime)
        self.assertIsInstance(mynew_review.name, str)
        self.assertIsInstance(mynew_review.my_number, int)
        self.assertEqual(actual_output, expected_output)
        self.assertDictEqual(actual_output_dict, expected_output_dict)

    def test_time(self):
        sleep(0.05)
        new = Review()
        self.assertNotEqual(new.created_at, self.shared_review.created_at)
        self.assertLess(self.shared_review.created_at, new.created_at)
        sleep(0.05)
        new.save()
        self.assertNotEqual(new.created_at, new.updated_at)
        self.assertLess(new.created_at, new.updated_at)

if __name__ == '__main__':
    unittest.main()
