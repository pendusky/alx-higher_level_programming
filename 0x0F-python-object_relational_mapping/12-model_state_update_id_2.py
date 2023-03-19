#!/usr/bin/python3
"""This module contains functions
    that update the name of the object with id equal to 2.
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
    """Performs a query that returns the object with id equal to 2.
    """
    obj = session.query(State).order_by(State.id).filter(
        State.id == 2).first()

    return obj


def update_object(session, obj):
    """Update the name of the object given by argument.
    """
    obj.name = "New Mexico"
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
    obj = query(session)
    update_object(session, obj)

    session.close()


if __name__ == "__main__":
    main_method()
