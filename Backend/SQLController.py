import sqlite3


def execute_query(query, cursor):
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return rows
    except sqlite3.Error as e:
        print("SQLite Error:", str(e)) 
        return []




