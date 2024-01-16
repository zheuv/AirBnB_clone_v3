#!/usr/bin/python3
import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class test_FileStorage(unittest.TestCase):
  fs = FileStorage()
  model = BaseModel()

  def test_type_objects(self):
    self.assertEqual(type(self.fs._FileStorage__objects), dict)

  def test_type_file_path(self):
    self.assertEqual(type(self.fs._FileStorage__file_path), str)
