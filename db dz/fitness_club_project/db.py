import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "..","fitness_club.db")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()