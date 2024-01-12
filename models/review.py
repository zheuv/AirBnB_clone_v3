#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """User class that inherits from BaseModel."""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialization of User class."""
        super().__init__(*args, **kwargs)
