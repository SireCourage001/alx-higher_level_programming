#!/usr/bin/python3
"""This script list all states starting with N,
from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    """In order to put our new connnection to good use we
     need to create a cursor object"""
    cur = db.cursor()
    """The execute function requires one parameter, the query."""
    cur.execute("SELECT * FROM states\
        WHERE name REGEXP BINARY '^N'\
            ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    """ Close all cursors"""
    cur.close()
    """Close all databases"""
    db.close()