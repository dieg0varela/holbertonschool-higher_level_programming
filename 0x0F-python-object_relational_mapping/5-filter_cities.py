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
    ret = ""

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=passwd, db=db_name, charset="utf8")
    cursor = db.cursor()
    querry = ("SELECT cities.name FROM cities JOIN states ON " +
              "cities.state_id=states.id WHERE states.name=%s " +
              "ORDER BY cities.id")
    params = (state,)
    cursor.execute(querry, params)
    res = cursor.fetchone()
    while res:
        ret += res[0] + ", "
        res = cursor.fetchone()
    print(ret[:-2])
    cursor.close()
    db.close()
