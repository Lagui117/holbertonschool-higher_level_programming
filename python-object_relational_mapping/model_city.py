#!/usr/bin/python3
"""
Module that defines the City class.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class that represents the cities table.

    Attributes:
        id: Auto-generated unique integer, primary key
        name: String with maximum 128 characters
        state_id: Integer, foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
