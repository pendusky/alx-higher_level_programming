#!/usr/bin/python3
"""This module contains functions that print the objects that
    name is equal to the given match.
    (If no state has the name you searched for, display Not found)
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def connect_to_database(host, port, user, password, database):
    """Connect to a specific database.
    Returns:
        session: sqlalchemy session.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'
                           .format(user, password,
                                   host, port, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    return session


def query(session, match):
    """Performs a "SELECT" query that print the objects that
        name is equal to the given match.
        (If no state has the name you searched for, display Not found)
    """
    query = session.query(State).order_by(State.id).filter(
        State.name == match).first()
    if query is not None:
        print("{}".format(query.id))
    else:
        print("Not found")


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

    session = connect_to_database(host, port, user, password, database)
    query(session, match)

    session.close()


if __name__ == "__main__":
    main_method()
