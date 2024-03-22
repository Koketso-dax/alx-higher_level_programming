#!/usr/bin/python3
""" Module for python func to login and read data from sql db """
import MySQLdb
import sys


def list_states(username, password, database):
    """
    Function to list states from a MySQL database.

    Args:
        username (str): The username to connect to the MySQL database.
        password (str): The password to connect to the MySQL database.
        database (str): The name of the MySQL database.

    Returns:
        None

    Prints:
        Prints the fetched data from the 'states' table in the database.

    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to fetch all states, sorted by states.id
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all the rows using fetchall() method
    data = cursor.fetchall()

    # Display the results
    for row in data:
        print(row)

    # Disconnect from server
    db.close()


if __name__ == "__main__":
    # Get MySQL username, password & db name from command line arguments
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to list states
    list_states(username, password, database)
