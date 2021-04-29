import sqlite3


def tables(DB_OBJ):
    result = [' ']
    CONN = sqlite3.connect(DB_OBJ)
    CURSOR = CONN.cursor()
    for row in CURSOR.execute(
            'SELECT name FROM sqlite_master where type="table"'):
        result.append(row[0])
    return result
