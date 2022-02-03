"""4"""
import sqlite3

def read_songs():
    conn = sqlite3.connect(
        "/home/ben/Desktop/Just-IT/python/week11/project/MusicDB.db"
        )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM songs;")
    row = cursor.fetchall()
    for record in row:
        print(record)
    # return record


# read_songs()
