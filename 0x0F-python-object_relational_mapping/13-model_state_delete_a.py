#!/usr/bin/python3
""" A script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa """

from sqlalchemy import create_engine, text, delete
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    usr, pwd, db = argv[1:]

    engine = create_engine(f"mysql+mysqldb://{usr}:{pwd}@localhost/{db}")
    Session = sessionmaker()
    session = Session(bind=engine)

    stmt = delete(State).where(State.name.like('%a%'))

    with session.begin():
        session.execute(stmt)
