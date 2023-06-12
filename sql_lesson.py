import sqlite3

with sqlite3.connect('test.db') as connection:
    cursor = connection.cursor()
    cursor.execute()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS country(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            population INTEGER 
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            address TEXT,
            email TEXT,
            country_id INTEGER NOT NULL DEFAULT 0,
            balance REAL NOT NULL DEFAULT 0,
            FOREIGN KEY (country_id) REFERENCES country(id)
        );
    """)
