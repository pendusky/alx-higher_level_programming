#!/usr/bin/python3
"""This module contains functions that lists all states from
    a specific database.
"""
import MySQLdb
import sys


def main_method():
    """It receives the input parameters and sends them to the
        corresponding methods.
    """
    args = sys.argv

    host = "localhost"
    port = 3306
    user = args[1]
    password = args[2]
    database = args[3]

    db = connect_to_database(host, port, user, password, database)
    cur = db.cursor()

    query(cur)

    cur.close()
    db.close()


def connect_to_database(host, port, user, password, database):
    """Connect to a specific database.
    Returns:
        db: database object.
    """
    db = MySQLdb.connect(host=host, port=port, passwd=password,
                         user=user, db=database)
    return db


def query(cur):
    """Performs a "SELECT" query that lists all states.
    """
    cur.execute("""SELECT * FROM states ORDER BY id ASC""")
    for row in cur.fetchall():
        print(row)


if __name__ == "__main__":
    main_method()
