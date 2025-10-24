#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    Connects to the database, retrieves and displays the first State object,
    sorted by states.id in ascending order.
    If the table is empty, prints "Nothing".
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

    # Query for the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Print the result or "Nothing" if no state is found
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()