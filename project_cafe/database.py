import sqlite3

conn = sqlite3.connect('cafe.db')
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY,
    name TEXT,
    balance REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    duration INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    client_name TEXT,
    service_name TEXT,
    price REAL
)
""")

conn.commit()
conn.close()

print("Таблиці створені")
