#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import models
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state', cascade='delete')

    @property
    def cities(self):
        """returns list of city instances with  matching state_id"""
        cities = models.storage.all(models.City)
        return [c for c in cities.values() if c.state_id == self.id]
