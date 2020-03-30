#!/usr/bin/python3
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine("mysql+mysqldb://{0}:{1}@localhost:3306/{2}".
                           format(username, password, db_name),
                           encoding='latin1', echo=True, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id):
        print("{0}: {1}".format(instance.id, instance.name))
