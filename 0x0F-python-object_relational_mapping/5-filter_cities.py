#!/usr/bin/python3
"""Script to list all cities of a given state from the database"""

import MySQLdb
import sys


def list_cities_of_state(username, password, database, state_name):
    """
    Function to list all cities of a given state from the specified MySQL db.
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Execute SQL query to fetch all cities
        query = "SELECT cities.id, cities.name,\
                states.name FROM cities JOIN states ON\
                cities.state_id = states.id WHERE states.name = %s \
                ORDER BY cities.id ASC"
        cursor.execute(query, (state_name,))

        # Fetch all the rows using fetchall() method
        data = cursor.fetchall()

        # Display the results
        for row in data:
            print(row)

    except MySQLdb.Error as e:
        print("Error accessing MySQL database:", e)
        sys.exit(1)

    finally:
        # Disconnect from server
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    """ main script """
    if len(sys.argv) != 5:
        print("Usage: ./script_name.py <usr> <pwd> <db> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to list cities of the given state
    list_cities_of_state(username, password, database, state_name)
