"""6"""

import time
import sqlite3

def delete_songs():
    conn = sqlite3.connect(
        "/home/ben/Desktop/Just-IT/python/week11/project/c5Music.db"
        )
    cursor = conn.cursor()

    id_field = input("Enter the ID number of the record you want to delete (e.g. 1): ")

    try:
        cursor.execute(f"DELETE FROM songs WHERE SongID = {id_field}")
        conn.commit()
        print(f"Record {id_field} deleted")

        time.sleep(3)
        cursor.execute("SELECT * FROM songs")
        row = cursor.fetchall()
        for record in row:
            print(record)
        return row
    except:
        print(f"Song {id_field} not deleted")
    finally:
        conn.close()


# delete_songs()
