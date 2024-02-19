#!/usr/bin/python3
""" A script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
from sys import argv
from model_state import Base, State

if __name__ == '__main__':

    usr, pwd, db, state_name = argv[1:]

    engine = create_engine(f"mysql+mysqldb://{usr}:{pwd}@localhost/{db}")

    Session = sessionmaker()
    session = Session(bind=engine)

    result = session.execute(text("SELECT states.id FROM states "
                             "WHERE states.name LIKE :state;"),
                             {"state": state_name})

    state = result.fetchone()
    if state:
        print(state.id)
    else:
        print("Not found")
