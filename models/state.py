#!/usr/bin/python3
""" a class to sophisticate console """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class which inherits from BaseModel """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of State class."""
        super().__init__(*args, **kwargs)
