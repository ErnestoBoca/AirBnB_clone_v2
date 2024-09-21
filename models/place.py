#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table("place_amenity", Base.metadata,
            Column("place_id", String(60), ForeignKey("places.id"), primary_key=True),
            Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True)
    )

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="delete")    
    amenities = relationship("Amenity", secondary="place_amenity", backref="place_amenities", viewonly=False)
    

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)


    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            list_review = []
            for review in storage.all(Review):
                if review.place_id == self.id:
                    list_review.append(review)
            return list_review
        
        @property
        def amenities(self):
            list_amenity = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    list_amenity.append(amenity)
            return list_amenity

        @amenities.setter
        def amenities(self, amenity):
            if isinstance(Amenity, amenity):
                self.amenity_ids.append(amenity.id)
