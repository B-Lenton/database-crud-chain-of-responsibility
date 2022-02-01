"""3"""
import time
import sqlite3

# create subroutine to add songs
def add_songs():
    conn = sqlite3.connect(
        "/home/ben/Desktop/Just-IT/python/week11/project/c5Music.db"
        )
    cursor = conn.cursor()
    
    # create empty list - song details will be appended
    songs = []
    # songID field is auto-increment
    songID = cursor.lastrowid

    title = input("Enter song title: ")
    artist = input("Enter artist name: ")
    genre = input("Enter song genre: ")

    songs.append(songID)
    songs.append(title)
    songs.append(artist)
    songs.append(genre)

    try:
        cursor.execute("INSERT INTO songs VALUES(?, ?, ?, ?) ", songs)
        conn.commit()
        print("Song added")

        time.sleep(3)
        cursor.execute("SELECT * FROM songs")
        row = cursor.fetchall()
        for record in row:
            print(record)
        return row
    except:
        print(f"Song {title} not added")
    finally:
        conn.close()


# add_songs()
