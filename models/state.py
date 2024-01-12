#!/usr/bin/python3

from models.base_model import BaseModel


class state(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of User class."""
        super().__init__(*args, **kwargs)
