#!/usr/bin/python3
'''List all States using SQLAlchemy'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).order_by(State.id)
    res = instance.first()
    if res:
        print(str(res.id) + ": " + res.name)
    else:
        print("Nothing")
