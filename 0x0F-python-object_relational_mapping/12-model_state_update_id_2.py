#!/usr/bin/python3
"""
Changes the name of a State object in the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:4]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    # Create session maker bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the State object with id = 2
    state = session.query(State).filter_by(id=2).first()

    if state:
        # Change the name of the state
        state.name = "New Mexico"

        # Commit the session to save changes to the database
        session.commit()
        print("State name changed successfully")
    else:
        print("State with id 2 not found")

    # Close session
    session.close()
