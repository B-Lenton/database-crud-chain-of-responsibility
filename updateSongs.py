"""5"""
import time
import sqlite3

def update_songs():
    conn = sqlite3.connect(
        "/home/ben/Desktop/Just-IT/python/week11/project/c5Music.db"
        )
    cursor = conn.cursor()

    id_field = input("Enter the ID number of the record you want to update (e.g. 1): ")
    field_name = input("Enter the field to be updated (Title, Artist, Genre): ")
    new_value = input("Enter a new value for the field: ")
    print(f"User value: '{new_value}'")

    try:
        cursor.execute(f"UPDATE songs SET {field_name} = '{new_value}' WHERE SongID = {id_field}")
        conn.commit()
        print(f"Record {id_field} updated")

        time.sleep(3)
        cursor.execute("SELECT * FROM songs")
        row = cursor.fetchall()
        for record in row:
            print(record)
        return row
    except:
        print(f"Song {id_field} not updated")
    finally:
        conn.close()


# update_songs()
