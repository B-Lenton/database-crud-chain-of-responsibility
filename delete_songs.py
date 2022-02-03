"""6"""

import time
import sqlite3

def delete_songs():
    conn = sqlite3.connect(
        "/home/ben/Desktop/Just-IT/python/week11/project/MusicDB.db"
        )
    cursor = conn.cursor()

    delete_song_name = input("Enter the name of the song you wish to delete: ")

    try:
        # search and display song
        cursor.execute("SELECT * FROM songs WHERE Title = ?", (delete_song_name,))
        conn.commit()
        row = cursor.fetchone()
        print(row)
        check_delete = input("Is this the song you want to delete? (Y/N) ")
        if check_delete.upper() in ["Y", "YES", "YE"]:
            cursor.execute("DELETE FROM songs WHERE Title = ?", (delete_song_name,))
            conn.commit()
            print(f"{delete_song_name} deleted.")
        else:
            print("No records deleted")

        print("Loading...")
        time.sleep(3)
        cursor.execute("SELECT * FROM songs")
        row = cursor.fetchall()
        for record in row:
            print(record)
        return row
    except:
        print(f"{delete_song_name} not deleted.")
    finally:
        conn.close()


# delete_songs()
