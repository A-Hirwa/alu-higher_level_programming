#!/usr/bin/python3
"""displays all the states"""
import MySQLdb
import sys

if __name__ == "__main__":
    """starting the connection"""
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )

    cr = db.cursor()
    cr.execute("""SELECT * FROM states WHERE name
            LIKE BINARY 'N%' ORDER BY states.id""")
    tables = cr.fetchall()
    for i in tables:
        print(i)
    cr.close()
<<<<<<< HEAD
    db.close()
=======
    db.close()
>>>>>>> e044d0c9abbbf6b0dc41108d29ad1a6d98fce128