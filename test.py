import sqlite3

conn = sqlite3.connect('website/db.sqlite3')
c = conn.cursor()
c.execute('SELECT * FROM main_post')
for row in c:
    print(row)
