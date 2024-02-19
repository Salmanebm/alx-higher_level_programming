#!/usr/bin/python3
""" A script that prints the first State object from the
database hbtn_0e_6_usa """

from sqlalchemy import create_engine, text
from sys import argv

if __name__ == '__main__':
    from model_state import Base, State

    usr, pwd, db = argv[1:]

    engine = create_engine(f"mysql+mysqldb://{usr}:{pwd}@localhost/{db}")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT states.id, states.name FROM states"
                                   " ORDER BY states.id LIMIT 1;"))
        state = result.fetchone()

    if state is not None:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
