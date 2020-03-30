#!/usr/bin/python3
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(username, password, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.id == 1)
    states = query.all()

    if not State.id:
        print("{:s}".format("Nothing"))
    for state in states:
        print("{:d}: {:s}".format(state.id, state.name))

    session.close()
