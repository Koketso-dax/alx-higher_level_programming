#!/usr/bin/python3
"""Script to display values in the states table based on user input"""

import MySQLdb
import sys


def search_state(username, password, database, state_name):
    """
    Function to search for a state in the states table based on user input.

    Args:
        username (str): The username to connect to the MySQL database.
        password (str): The password to connect to the MySQL database.
        database (str): The name of the MySQL database.
        state_name (str): The name of the state to search for.

    Returns:
        None

    Prints:
        Prints the fetched data from the 'states' table in the database.

    Raises:
        MySQLdb.Error: If there is an error accessing the MySQL database.
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

        # Execute SQL query to fetch states matching the input state name
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
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
    # Get MySQL username, password, database name, and state name from command
    # line arguments
    if len(sys.argv) != 5:
        print("Usage: ./script_name.py <usr> <pwd> <db> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to search for the state
    search_state(username, password, database, state_name)
