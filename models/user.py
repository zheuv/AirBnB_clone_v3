#!/usr/bin/python3
""" a class to sophisticate console """
from models.base_model import BaseModel, Base
from sqlalchemyorm import Column, String
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

class User(BaseModel, Base):
    """User class that inherits from BaseModel and Base."""
    __tablename__ = "users"
    if storage_type == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
