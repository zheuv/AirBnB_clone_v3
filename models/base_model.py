#!/usr/bin/python3
import uuid
import datetime
import models

class BaseModel:
    def __init__(self, **kwargs):
        """Initialization of BaseModel Class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        if kwargs:
            for (key, value) in kwargs.items():
                if key != '__class__':
                    if (key == "created_at" or key == "updated_at"):
                        format_string = "%Y-%m-%dT%H:%M:%S.%f"
                        value = datetime.datetime.strptime(value, format_string)
                    setattr(self, key, value)
        else:
            models.storage.new(self)
    def __str__(self):
        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))
    def save(self):
        self.updated_at = datetime.datetime.today()
        models.storage.save()

    def to_dict(self):
        dicti = dict()
        dicti["__class__"] = "BaseModel"
        for key in self.__dict__.keys():
            value = getattr(self, key)
            if type(value) is datetime.datetime:
                value = value.isoformat()
            dicti[key] = value
        return dicti

