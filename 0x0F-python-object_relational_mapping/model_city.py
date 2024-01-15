#!/usr/bin/python3
"""This script shows python file that contains the class definition of a
State and an instance Base = declarative_base()"""

from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base



class City(Base):
    """A class City from Base"""

  __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
