#!/usr/bin/python3
"""
Takes argument and displays all values in the states
table where name matches the argument.
Your scripts should take 4 arguements: mysql username, password,
database name and state name.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         password=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY \
                   id ASC".format(argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
