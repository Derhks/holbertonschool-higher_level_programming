#!/usr/bin/python3
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine("mysql+mysqldb://{0}:{1}@localhost:3306/{2}".
                           format(username, password, db_name),
                           encoding='latin1', echo=True, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with engine.connect() as connection:
        result = connection.execute("SELECT states.id, states.name\
                                    FROM states ORDER BY states.id ASC")
        for row in result:
            cnt = 0
            for items in row:
                if cnt == 0:
                    print("{}".format(items), end=": ")
                else:
                    print("{}".format(items), end="")
                cnt += 1
            print()
