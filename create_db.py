"""2"""
import sqlite3  # import SQLite library (comes with Python)

conn = sqlite3.connect(
    "/home/ben/Desktop/Just-IT/python/week11/project/MusicDB.db"
    )  # create and/or connect to database
cursor = conn.cursor()

cursor.execute("""
INSERT INTO songs ('Title', 'Artist', 'Genre') VALUES 
    ('Rockstar', 'Nickelback', 'Rock'),
    ('I bet that you look good on the dancefloor', 'Arctic Monkeys', 'Rock'),
    ('Grenade', 'Bruno Mars', 'Pop'),
    ('Our House', 'Madness', 'Ska'),
    ('All Blues', 'Miles Davis', 'Blues'),
    ('Feel the Love', 'Rudimental', 'Dance'),
    ('Blank Space', 'Taylor Swift', 'Pop'),
    ('Slim Shady', 'Eminem', 'Hip Hop'),
    ('Love Me Again', 'John Newman', 'Pop'),
    ('Back in Black', 'AC/DC', 'Rock'),
    ('When the Levee Breaks', 'Led Zepellin', 'Rock'),
    ('Smash Mouth', 'All Star', 'Cheese'),
    ('Three Little Birds', 'Bob Marley', 'Dub'),
    ('All I Ever Wanted', 'Basshunter', 'Dance'),
    ('Everywhere', 'Fleetwood Mac', 'Rock'),
    ('Baggy Trousers', 'Madness', 'Ska'),
    ('Time', 'Supergrass', 'Rock'),
    ('Love the way you lie', 'Eminem & Rhianna', 'RnB');
"""
)
conn.commit()


# create tables
# ...............................
# cursor.execute("""
# CREATE VIRTUAL TABLE songs
# 	USING FTS5 (
# 		Title,
# 		Artist,
# 		Genre
# 	);"""
# )
# ...............................
# cursor.execute("""
# CREATE TABLE "songs" (
# 	"SongID"	INTEGER NOT NULL UNIQUE,
# 	"Title"	TEXT,
# 	"Artist"	TEXT,
# 	"Genre"	TEXT,
# 	PRIMARY KEY("SongID" AUTOINCREMENT)
# )"""
# )
# ...........................
# cursor.execute("""

#   CREATE TABLE "downloads" (
# 	"DownlID"	INTEGER NOT NULL UNIQUE,
# 	"SongID"	INTEGER,
# 	"MemberID"	INTEGER,
# 	"Date"	TEXT,
# 	PRIMARY KEY("DownlID" AUTOINCREMENT),
# 	FOREIGN KEY("SongID") REFERENCES "songs"("SongID"),
# 	FOREIGN KEY("MemberID") REFERENCES "members"("MemberID")
# )
# """)
