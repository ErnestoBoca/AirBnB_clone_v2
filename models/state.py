#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
#from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    #cities = relationship("City", cascade="all, delete")
    cities = relationship('City', backref='state', cascade='delete')

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """returns the list o cities with the state_id equals to the curresnt
            State.id"""
            from models import storage
            list_cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    list_cities.append(city)

            return list_cities
