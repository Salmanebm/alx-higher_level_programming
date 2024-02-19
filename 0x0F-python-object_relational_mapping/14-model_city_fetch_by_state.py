#!/usr/bin/python3
""" A script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa """

from model_city import Base, City
from model_state import State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    usr, pwd, db = argv[1:]

    engine = create_engine(f"mysql+mysqldb://{usr}:{pwd}@localhost/{db}")

    Session = sessionmaker()
    session = Session(bind=engine)

    stmt = select(City.name, City.id, State.name).join_from(City, State)\
        .order_by(City.id)

    with session.begin():
        result = session.execute(stmt)

    for row in result:
        print(f"{row[2]}: ({row[1]}) {row[0]}")
