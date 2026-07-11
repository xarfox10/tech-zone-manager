from database.database import Database


class IdRepository:

    def __init__(self):
        self.database = Database()

    def get_next_number(self, prefix):

        self.database.cursor.execute(
            """
            SELECT next_number
            FROM id_counter
            WHERE prefix = ?
            """,
            (prefix,),
        )

        row = self.database.cursor.fetchone()

        return row[0]
        
    def update_next_number(self, prefix, next_number):

        self.database.cursor.execute(
            """
            UPDATE id_counter
            SET next_number = ?
            WHERE prefix = ?
            """,
            (next_number, prefix),
        )

        self.database.connection.commit()