#!/usr/bin/python3
""" the BaseModel class implementation """
import uuid
import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

class BaseModel:
    """ the BaseModel class """
    id = Column(String(60), primary_key=True,
                nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)
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

    def __str__(self):
        """ Returns the str repr of an instance """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ updates updated_at and savesthe changes in the json file """
        self.updated_at = datetime.datetime.today()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ Returns the dict repr of an instance """
        dicti = dict()
        dicti["__class__"] = self.__class__.__name__
        for key in self.__dict__.keys():
            if key != "_sa_instance_state":
                value = getattr(self, key)
                if type(value) is datetime.datetime:
                    value = value.isoformat()
                dicti[key] = value
        return dicti

    def delete(self):
        """deletes an instance """
        models.storage.delete(self)
