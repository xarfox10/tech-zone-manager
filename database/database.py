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

        self.initialize_id_counters()
        self.connection.commit()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS id_counter (

            prefix TEXT PRIMARY KEY,

            next_number INTEGER

            )
        """)

    def initialize_id_counters(self):

        default_prefixes = [
            "TZ",
            "SL",
            "PO",
            "RP",
            "CU",
            "SP",
        ]

        for prefix in default_prefixes:

            self.cursor.execute(
                """
                INSERT OR IGNORE INTO id_counter
                (prefix, next_number)

                VALUES (?, ?)
                """,
                (prefix, 1),
            )