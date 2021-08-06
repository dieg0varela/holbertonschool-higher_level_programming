#!/usr/bin/python3
'''List all states in the DB'''
import MySQLdb
import sys
argv = sys.argv

if (__name__ == "__main__"):
    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    state = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=passwd, db=db_name, charset="utf8")
    cursor = db.cursor()
    querry = ("SELECT * FROM states WHERE name=%s ORDER BY id")
    params = (state,)
    cursor.execute(querry, params)
    res = cursor.fetchall()
    for item in res:
        print(item)
    cursor.close()
    db.close()
