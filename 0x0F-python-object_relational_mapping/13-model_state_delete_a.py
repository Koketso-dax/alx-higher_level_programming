#!/usr/bin/python3
"""
Deletes all State with char a from the database hbtn_0e_6_usa
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

    # Query and delete all State objects with a name containing the letter 'a'
    states_to_delete = session.query(State)
    .filter(State.name.like('%a%')).all()
    if states_to_delete:
        for state in states_to_delete:
            session.delete(state)
        session.commit()
    else:
        print("No states found containing the letter 'a'")

    # Close session
    session.close()
