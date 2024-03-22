#!/usr/bin/python3
"""Start link class to table in database"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class representing a state in the database.

        Attributes:
            __tablename__ (str): The table name of the class
            id (int): The State id of the class
            name (str): The State name of the class
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
