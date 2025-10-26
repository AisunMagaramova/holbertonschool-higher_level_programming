#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to the database
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cur = db.cursor()

    # Retrieve all states sorted by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
