#!/usr/bin/python3
""" a class to sophisticate console """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """City class that inherits from BaseModel."""
    __tablename__ = "cities"
    if storage_type == "db":
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", cascade="all,delete", backref="cities")
    else:
        state_id = ""
        name = ""
