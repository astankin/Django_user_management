import sqlite3

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()
result = cur.execute("SELECT * FROM auth_user")
for elem in result:
    print(elem)