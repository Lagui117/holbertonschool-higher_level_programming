#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    Connects to the database, retrieves and displays all State objects
    containing the letter 'a', sorted by states.id in ascending order.
    """
    # Create the engine to connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Bind the engine to the metadata of the Base class
    Base.metadata.create_all(engine)

    # Create a configured "Session" class and instantiate a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for State objects containing the letter 'a'
    states = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id)
        .all()
    )

    # Print each state in the required format
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()