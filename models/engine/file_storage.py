#!/usr/bin/python3

""" Doc Here """
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = dict()
    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
    def save(self):
        serialized_objects = dict()
        for key, obj in FileStorage.__objects.items() :
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)
    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, data in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_class = eval(class_name)
                    obj_instance = obj_class(**data)
                    FileStorage.__objects[key] = obj_instance
            



