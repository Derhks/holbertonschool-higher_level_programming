#!/usr/bin/python3
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(username, password, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name == state_name).\
        order_by(State.id)
    states = query.all()

    if not states:
        print("{:s}".format("Not found"))
    else:
        for state in states:
            print("{:d}".format(state.id))

    session.close()
