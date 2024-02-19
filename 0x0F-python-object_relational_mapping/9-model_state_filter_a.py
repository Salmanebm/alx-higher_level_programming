#!/usr/bin/python3
""" A script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa """

from sqlalchemy import create_engine, text
from sys import argv
from model_state import Base, State

if __name__ == '__main__':

    usr, pwd, db = argv[1:]

    engine = create_engine(f"mysql+mysqldb://{usr}:{pwd}@localhost/{db}")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT states.id, states.name FROM states"
                              " WHERE name LIKE '%a%' ORDER BY states.id;"))

    for state in result:
        print(f"{state.id}: {state.name}")
