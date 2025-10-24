#!/usr/bin/python3
"""
Lists all cities of a state passed as argument from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connects to the database,
    retrieves and displays all cities of a given state,
    sorted by cities.id in ascending order.
    """
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # SQL query to retrieve all cities of the given state
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """
    cursor.execute(query, (sys.argv[4],))

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Print the city names as a comma-separated list
    print(", ".join(row[0] for row in rows))

    # Close the cursor and database connection
    cursor.close()
    db.close()