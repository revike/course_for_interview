import os
import sqlite3

DB_OBJ = os.path.join(os.path.dirname(__file__), "db.sqlite3")

CONN = sqlite3.connect(DB_OBJ)

CURSOR = CONN.cursor()


for row in CURSOR.execute('SELECT * FROM Categories'):
    print(row)
