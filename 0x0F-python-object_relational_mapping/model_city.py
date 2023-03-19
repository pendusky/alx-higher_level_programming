#!/usr/bin/python3
"""This module contains a class that defines the City class.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """Definition of a City class.
    Args:
        Base : base class.
    """
    __tablename__ = 'cities'

    id = Column('id', Integer, nullable=False,
                autoincrement=True, unique=True, primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'),
                      nullable=False)
    state = relationship("State")

