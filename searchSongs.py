"""7"""
import sqlite3

def search_songs():
    conn = sqlite3.connect(
        "/home/ben/Desktop/Just-IT/python/week11/project/c5Music.db"
        )
    cursor = conn.cursor()

    song_name = input("Enter the song you want to search for: ")
    print(f"Search for: '{song_name}'")

    try:
        cursor.execute(f"SELECT * FROM songs WHERE Title = '{song_name}'")
        conn.commit()
        row = cursor.fetchall()
        for record in row:
            print(record)
        return row
    except:
        print(f"Song {song_name} not found")
    finally:
        conn.close()

# while True:
#     search_songs()
