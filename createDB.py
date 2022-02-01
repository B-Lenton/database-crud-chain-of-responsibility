"""2"""
import sqlite3  # import SQLite library (comes with Python)

conn = sqlite3.connect(
    "/home/ben/Desktop/Just-IT/python/week11/project/c5Music.db"
    )  # create and/or connect to database
cursor = conn.cursor()

# create tables
# ...............................
cursor.execute("""

CREATE TABLE "members" (
	"MemberID"	INTEGER NOT NULL UNIQUE,
	"Firstname"	TEXT,
	"Lastname"	TEXT,
	"Email"	TEXT,
	PRIMARY KEY("MemberID" AUTOINCREMENT)
)"""
)
# ...............................
cursor.execute("""
CREATE TABLE "songs" (
	"SongID"	INTEGER NOT NULL UNIQUE,
	"Title"	TEXT,
	"Artist"	TEXT,
	"Genre"	TEXT,
	PRIMARY KEY("SongID" AUTOINCREMENT)
)"""
)
# ...........................
cursor.execute("""

  CREATE TABLE "downloads" (
	"DownlID"	INTEGER NOT NULL UNIQUE,
	"SongID"	INTEGER,
	"MemberID"	INTEGER,
	"Date"	TEXT,
	PRIMARY KEY("DownlID" AUTOINCREMENT),
	FOREIGN KEY("SongID") REFERENCES "songs"("SongID"),
	FOREIGN KEY("MemberID") REFERENCES "members"("MemberID")
)
""")
