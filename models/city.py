#!/usr/bin/python3
""" a class to sophisticate console """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey


class City(BaseModel, Base):
    """City class that inherits from BaseModel."""
    __tablename__ = "cities"
    
    state_id = Column(String(60), ForeignKey('states.id')
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialization of City class."""
        super().__init__(*args, **kwargs)
