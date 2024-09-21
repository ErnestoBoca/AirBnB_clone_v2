#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)


    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
