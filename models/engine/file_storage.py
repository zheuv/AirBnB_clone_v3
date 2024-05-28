#!/usr/bin/python3

""" Doc for file_storage """
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
    """ FileStorage class """
    __file_path = "file.json"
    __objects = dict()
    list = ["User", "Amenity", "Place", "City", "State", "Review"]
    def all(self, cls=None):
        """ returns the dictionary __objects """
        if cls is not None:
            dicti = dict()
            for key, value in FileStorage.__objects.items():
                k = key.split('.')
                if k[0] == cls.__name__:
                    dicti[key] = value
            return dicti       
        return FileStorage.__objects

    def get(self, cls, id):
        """ Returns an instance """
        if (cls is not None) and (id is not None):
            dicti = dict()
            cls.id = cls.__name__  + '.' + id
            for key, value in FileStorage.__objects.items():
                if key == cls.id:
                    return str(value)
        return None
    def count(self, cls=None):
        """ Retruns the number of instances """
        n = 0
        if cls is not None:
            if cls in self.list:
                for key in FileStorage.__objects.keys():
                    k = key.split('.')
                    if k[0] == cls.__name__:
                        n = n + 1
            return n
        return len(FileStorage.__objects)

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def delete(self, obj=None):
        """ deletes an object from objects """
        if obj != None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            del FileStorage.__objects[key]

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        serialized_objects = dict()
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised) """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, data in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_class = eval(class_name)
                    obj_instance = obj_class(**data)
                    FileStorage.__objects[key] = obj_instance
