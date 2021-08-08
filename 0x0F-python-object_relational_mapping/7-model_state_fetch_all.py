#!/usr/bin/python3
'''List all States using SQLAlchemy'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    for instance in session.query(State).order_by(State.id):
        print(str(instance.id) + ": " + instance.name)
