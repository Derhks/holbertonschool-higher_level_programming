#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    # prepare a cursor object using cursor() method
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities, states WHERE cities.state_id = states.id\
                ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
