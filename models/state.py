#!/usr/bin/python3
""" a class to sophisticate console """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class which inherits from BaseModel """
    __tablename__ = "states"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all,delete", backref="state")
    else:
        name = ""
        @getter
        def cities(self):
            from models import storage
            list = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                list.append(city)
            return list
