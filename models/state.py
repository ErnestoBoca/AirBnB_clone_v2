#!/usr/bin/python3
""" State Module for HBNB project """
from models import type_storage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    if type_storage == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)


    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """returns the list o cities with the state_id equals
            to the current State.id""" 
            list_cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    list_cities.append(city)

            return list_cities
