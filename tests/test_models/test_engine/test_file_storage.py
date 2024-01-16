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
  def test_type_fs(self):
    self.assertEqual(type(self.fs), Filestorage)

  def test_type_objects(self):
    self.assertEqual(type(self.fs._FileStorage__objects), dict)

  def test_type_file_path(self):
    self.assertEqual(type(self.fs._FileStorage__file_path), str)

  def test_new(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + cy.id, models.storage.all().keys())
        self.assertIn(cy, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())
  def test_new_with_args(self):
    with self.assertRaises(TypeError):
      models.storage.new(BaseModel(), 1)
  def test_save(self):
    bm = BaseModel()
    us = User()
    st = State()
    pl = Place()
    cy = City()
    am = Amenity()
    rv = Review()
    models.storage.new(bm)
    models.storage.new(us)
    models.storage.new(st)
    models.storage.new(pl)
    models.storage.new(cy)
    models.storage.new(am)
    models.storage.new(rv)
    models.storage.save()
    save_text = ""
    with open("file.json", "r") as f:
      save_text = f.read()
      self.assertIn("BaseModel." + bm.id, save_text)
      self.assertIn("User." + us.id, save_text)
      self.assertIn("State." + st.id, save_text)
      self.assertIn("Place." + pl.id, save_text)
      self.assertIn("City." + cy.id, save_text)
      self.assertIn("Amenity." + am.id, save_text)
      self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
