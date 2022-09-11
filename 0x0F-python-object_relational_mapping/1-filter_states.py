#!/usr/bin/python3

"""
List all states with name string with N from db hbtn_0e_0_usa.
Takes 3 three arguements: mysql username, password and db name.
results shuould connect toa mysql server on running localhost.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         password=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close()
