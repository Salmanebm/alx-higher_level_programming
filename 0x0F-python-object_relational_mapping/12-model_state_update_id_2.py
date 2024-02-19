#!/usr/bin/python3
""" A script that changes the name of a State object
from the database hbtn_0e_6_usa """

from model_state import Base, State
from sqlalchemy import create_engine, text, update
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':

    usr, pwd, db = argv[1:]

    engine = create_engine(f"mysql+mysqldb://{usr}:{pwd}@localhost/{db}")

    Session = sessionmaker()
    session = Session(bind=engine)

    stmt = (update(State).where(State.id == 2).values(name="New Mexico"))

    with session.begin():
        session.execute(stmt)
