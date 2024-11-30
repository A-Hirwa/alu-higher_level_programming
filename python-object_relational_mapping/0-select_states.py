#!/usr/bin/python3
<<<<<<< HEAD
""" displays all the cities"""
import sys
import MySQLdb

if __name__ == "__main__":
    """ starting with the connection"""
    with MySQLdb.connect(
=======
"""
    Create a script that lists all states from a database hbtn_0e_0_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db_conn = MySQLdb.connect(
>>>>>>> e044d0c9abbbf6b0dc41108d29ad1a6d98fce128
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
<<<<<<< HEAD
    )as s:
        cur = s.cursor()
        cur.execute(
                "SELECT * FROM states ORDER BY id ASC"
            )
        all_states = cur.fetchall()
        for each_state in all_states:
            print(each_state)
        cur.close()
=======
    )

    cur = db_conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db_conn.close()
>>>>>>> e044d0c9abbbf6b0dc41108d29ad1a6d98fce128
