#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connects to the database, retrieves and displays all states
    with a name starting with 'N' in ascending order by states.id.
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

    # Execute the SQL query to retrieve states starting with 'N'
    cursor.execute("""
        SELECT * FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY states.id
    """)

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Print each row in the required format
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()