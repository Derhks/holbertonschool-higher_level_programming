#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    # prepare a cursor object using cursor() method
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name = '{:s}'\
                COLLATE latin1_general_cs\
                ORDER BY states.id ASC".format(state_name))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
