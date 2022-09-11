#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
The script should take 3 arguments: mysql username, mysql password and db name.
No arguement validation required.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
            password=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
