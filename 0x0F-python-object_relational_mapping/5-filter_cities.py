#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    # Open database connection
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)

    # prepare a cursor object using cursor() method
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities, states\
                WHERE states.name = %s AND states.id = cities.state_id\
                ORDER BY cities.id ASC", (state_name, ))
    rows = cur.fetchall()

    cnt = 0
    for row in rows:
        for city in row:
            if cnt < len(rows) - 1:
                print("{:s}".format(city), end=", ")
            else:
                print("{:s}".format(city), end="")
            cnt += 1
    print()

    cur.close()
    db.close()
