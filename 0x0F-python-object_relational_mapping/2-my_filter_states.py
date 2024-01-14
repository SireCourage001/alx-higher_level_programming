#!/usr/bin/python3

"""This script takes in an argument and displays all values in
 the states table of hbtn_0e_0_usa where name matches arguments"""

import MySQLdb
import sys

db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

cur = db.cursor()
    """The execute function requires one parameter, the query."""
    cur.execute("SELECT * FROM states\
        WHERE BINARY name = '{}'\
            ORDER BY id ASC".format(sys.argv[4]))

rows = cur.fetchall()
    for row in rows:
        print(row)
    """ Close all cursors"""
    cur.close()
    """Close all databases"""
    db.close()

if __name__ == "__main__": 
