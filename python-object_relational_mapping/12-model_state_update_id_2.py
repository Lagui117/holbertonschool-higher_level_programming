#!/usr/bin/python3
"""
Changes the name of a State object with id = 2
to "New Mexico" in the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    Connects to the database, updates the State object with id = 2,
    and sets its name to "New Mexico".
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

    # Query for the State object with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Update the state's name if it exists
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()