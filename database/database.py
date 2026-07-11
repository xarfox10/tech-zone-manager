import sqlite3

class Database:

    def __init__(self):
        self.connection = sqlite3.connect("tech_zone.db")
        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory (

                item_id TEXT PRIMARY KEY,

                name TEXT,

                category TEXT,

                stock INTEGER,

                price REAL,

                barcode TEXT

        )
    """)

        self.connection.commit()