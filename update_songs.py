"""5"""
import time
import sqlite3

def update_songs():
    conn = sqlite3.connect(
        "/home/ben/Desktop/Just-IT/python/week11/project/MusicDB.db"
        )
    cursor = conn.cursor()

    current_name = input("Enter the current name of the song you wish to update: ")
    
    try:
        # search and display song
        cursor.execute("SELECT * FROM songs WHERE Title = ?", (current_name,))
        conn.commit()
        row = cursor.fetchone()
        print(row)

        # Update record:
        if row is not None:
            new_title = input("Enter a new Title: ")
            new_artist = input("Enter a new Artist: ")
            new_genre = input("Enter a new Genre: ")
            cursor.execute("UPDATE songs SET Title = ?, Artist = ?, Genre = ? WHERE Title = ?", [new_title, new_artist, new_genre, current_name])
            conn.commit()
            
            print(f"{current_name} updated to {new_title}, {new_artist}, {new_genre}.")
            print("Loading...")
            
            time.sleep(3)
            cursor.execute("SELECT * FROM songs")
            row = cursor.fetchall()
            for record in row:
                print(record)
            return row
        not_found_msg = print("No songs found.")
        return not_found_msg
    except:
        print(f"Song '{current_name}' not updated")
    finally:
        conn.close()


# update_songs()
