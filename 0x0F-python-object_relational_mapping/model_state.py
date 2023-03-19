#!/usr/bin/python3
"""This module contains a class that defines the State class.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Definition of a State class.
    Args:
        Base : base class.
    """
    __tablename__ = 'states'

    id = Column('id', Integer, nullable=False,
                autoincrement=True, unique=True, primary_key=True)
    name = Column('name', String(128), nullable=False)
