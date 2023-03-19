#!/usr/bin/python3
"""This module contains functions that add a new object
    Louisiana to the database.
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


def query(session):
    """Performs a "SELECT" query that print the objects that name
        is equal to "Louisiana".
    """
    query = session.query(State).order_by(State.id).filter(
        State.name == "Louisiana").first()
    print("{}".format(query.id))


def adding_object(session):
    """Adding a new object (Louisiana) to the database.
    """
    Louisiana = State(name='Louisiana')
    session.add(Louisiana)
    session.commit()


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

    session = connect_to_database(host, port, user, password, database)
    adding_object(session)
    query(session)

    session.close()


if __name__ == "__main__":
    main_method()
