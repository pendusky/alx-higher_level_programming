#!/usr/bin/python3
"""This module contains functions that lists all cities of that state,
    using the specific database.
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
    """Performs a "SELECT" query that lists all cities of that state,
        using the specific database.
    """
    cur.execute("""SELECT cities.name FROM cities INNER JOIN states ON
                states.id=cities.state_id WHERE states.name=%s ORDER
                BY cities.id ASC""", (match,))
    r = []
    for row in cur.fetchall():
        r.append(row[0])
    print(", ".join(r))


if __name__ == "__main__":
    main_method()
