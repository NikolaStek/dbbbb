import sqlite3

conn = sqlite3.connect("cafe.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM orders")
orders = cursor.fetchall()
