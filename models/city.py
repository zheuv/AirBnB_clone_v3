#!/usr/bin/python3

from models.base_model import BaseModel


class city(BaseModel):
    """City class that inherits from BaseModel."""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of City class."""
        super().__init__(*args, **kwargs)
