#!/usr/bin/python3
"""This module contains functions that lists all states where name matches the
    argument from a specific database.
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
    match = args[4]

    db = connect_to_database(host, port, user, password, database)
    cur = db.cursor()

    query(cur, match)

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


def query(cur, match):
    """Performs a "SELECT" query that lists all states where name matches
        the argument "match".
    """
    cur.execute("""SELECT * FROM states WHERE
                name="{}" ORDER BY id ASC""".format(match))
    for row in cur.fetchall():
        if row[1] == match:
            print(row)


if __name__ == "__main__":
    main_method()
