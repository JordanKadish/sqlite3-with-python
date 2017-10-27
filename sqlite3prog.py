# Jordan Kadish
# 27/10/2017
# sqlite python database creation script
import sqlite3 as db

dbName = input("enter a database name (\"test.db\")\n")
try:
    # connect to an existing database
    # or create a new one with the name taken from input
    connect = db.connect(dbName)
    cursor = connect.cursor()
except Exception as e:
    print(e)

command = input("Enter SQL commands, or type \"end\" to exit\n")
while not (command == "end"):
    try:
        cursor.execute(command)
        response = cursor.fetchall()
        for row in response:
            print(row)
    except Exception as e:
        print(e)
    command = input()
