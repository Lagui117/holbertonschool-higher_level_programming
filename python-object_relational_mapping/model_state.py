#!/usr/bin/python3
"""
Module that defines the State class and Base instance.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that represents the states table.

    Attributes:
        id: Auto-generated unique integer, primary key
        name: String with maximum 128 characters
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
