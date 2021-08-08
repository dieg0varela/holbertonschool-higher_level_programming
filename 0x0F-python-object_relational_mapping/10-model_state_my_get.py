#!/usr/bin/python3
'''List all States using SQLAlchemy'''

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = (session.query(State).filter(text("states.name=('{}')"
                     .format(sys.argv[4]))).order_by(State.id))

    if instance.count() != 0:
        res = instance.all()
        print(res[0].id)
    else:
        print("Not Found")
