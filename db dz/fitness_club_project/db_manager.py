import sqlite3

conn = sqlite3.connect("fitness_club.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS memberships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    price REAL NOT NULL,
    duration INTEGER NOT NULL
)
""")

conn.commit()
conn.close()

print("Таблиці створені")
