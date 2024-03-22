#!/usr/bin/python3
"""Script to list all cities from the database"""

import MySQLdb
import sys


def list_cities(username, password, database):
    """
    Function to list all cities from the specified MySQL database.

    Args:
        username (str): The username to connect to the MySQL database.
        password (str): The password to connect to the MySQL database.
        database (str): The name of the MySQL database.

    Returns:
        None

    Prints:
        Prints the fetched data from the 'cities' table in the database.

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

        # Execute SQL query to fetch all cities sorted by cities.id
        cursor.execute("SELECT * FROM cities ORDER BY id ASC")

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
    # Get MySQL usr, pwd, and db name from command line args
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <usr> <pwd> <db>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to list cities
    list_cities(username, password, database)
