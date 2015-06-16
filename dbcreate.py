# -*- coding: utf-8 -*-

import sys, os
import sqlite3

def dbcreate():
    if not os.path.exists("config"):
        os.system("mkdir config")

    if not os.path.exists("config/location.db"):
        db = sqlite3.connect("config/location.db")
        sql = """
create table Location(
name varchar(10),
num integer
);
"""
        db.execute(sql)

        sql = "insert into Location values (?, ?)"
        for line in open("data.txt").readlines():
            line = line.split(",")
            db.execute(sql, (line[0].decode("utf8"), int(line[1].strip())))
        db.commit()
        db.close()

def getCityID(name):
    db = sqlite3.connect("config/location.db")
    id = 0
    for row in db.execute("select * from Location where name=\"%s\"" % name):
        id = row[1]
    db.close()
    if id == 0:
        print "Sorry, %s does not exist in DATABASE." % name
    else:
        # print "id: %d" % id
        pass
    return str(id).zfill(6)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Please input the city-name."
        sys.exit(1)

    name = sys.argv[1]
    dbcreate()
    getCityID(name)

