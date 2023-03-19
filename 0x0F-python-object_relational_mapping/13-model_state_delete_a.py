#!/usr/bin/python3
"""This module contains functions
    that delete all objects with a name containing the letter "a".
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
    """Performs a query that returns the objects with name
        containing the letter "a".
    """
    query = session.query(State).filter(State.name.contains("a"))
    obj_list = []
    for ob in query:
        obj_list.append(ob)

    return obj_list


def delete_objects(session, objs):
    """Delete the objects given by argument.
    """
    for obj in objs:
        session.delete(obj)
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
    objs = query(session)
    delete_objects(session, objs)

    session.close()


if __name__ == "__main__":
    main_method()
