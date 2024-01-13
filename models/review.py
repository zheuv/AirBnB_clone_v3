#!/usr/bin/python3
""" a class to sophisticate console """
from models.base_model import BaseModel


class Review(BaseModel):
    """User class that inherits from BaseModel."""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialization of Review class."""
        super().__init__(*args, **kwargs)
