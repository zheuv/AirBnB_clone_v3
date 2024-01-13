#!/usr/bin/python3
""" a class to sophisticate console """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of Amenity class."""
        super().__init__(*args, **kwargs)
