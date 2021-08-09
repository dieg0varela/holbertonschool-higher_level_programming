#!/usr/bin/python3
'''City Module Definition'''

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    '''City class'''
    __tablename__ = 'cities'
    id = Column('id', Integer, nullable=False, primary_key=True,
                autoincrement=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'), nullable=False)
