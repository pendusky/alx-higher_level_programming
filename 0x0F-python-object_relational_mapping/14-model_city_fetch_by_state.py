#!/usr/bin/python3
"""This module contains functions
    that prints all City objects from the database.
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City


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
    """Performs a query that prints all City objects from the database.
    """
    quer = session.query(City).join(State).order_by(City.id).all()
    for obj in quer:
        print("{}: ({}) {}".format(obj.state.name, obj.id, obj.name))


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
    query(session)

    session.close()


if __name__ == "__main__":
    main_method()

