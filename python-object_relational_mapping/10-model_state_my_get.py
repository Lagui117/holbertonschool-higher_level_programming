#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    Connects to the database, retrieves and displays the State object
    with the name passed as an argument.
    If no state is found, it prints "Not found".
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

    # Query for the State object with the given name
    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()

    # Print the result or "Not found" if no state is found
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
