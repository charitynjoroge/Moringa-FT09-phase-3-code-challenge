import sqlite3

CONN = sqlite3.connect('magazines.db')
CURSOR = CONN.cursor()