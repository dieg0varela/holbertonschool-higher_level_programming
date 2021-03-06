#!/usr/bin/python3
'''State Module Definition'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''State class'''
    __tablename__ = 'states'
    id = Column('id', Integer, nullable=False, primary_key=True,
                autoincrement=True)
    name = Column('name', String(128), nullable=False)
