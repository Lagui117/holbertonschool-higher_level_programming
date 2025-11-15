#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument, safe from SQL injection.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connects to the database, retrieves and displays all states
    where name matches the argument, sorted by states.id.
    This version is safe from SQL injection.
    """
    # Connect to the MySQL server on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query using parameterized queries to prevent injection
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Print each row in the required format
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
