#!/usr/bin/python3
""" a class to sophisticate console """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

class Review(BaseModel, Base):
    """User class that inherits from BaseModel."""
    __tablename__ = "reviews"
    if storage_type == "db":
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), nullable=False, ForeignKey("places.id"))
        user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
    else:
        place_id = ""
        user_id = ""
        text = ""
