from database.database import Database
from models.item import Item


class ItemRepository:

    def __init__(self):
        self.database = Database()

    def save(self, item):

        self.database.cursor.execute(
            """
            INSERT INTO inventory
            (
                item_id,
                name,
                category,
                stock,
                price,
                barcode
            )

            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                item.item_id,
                item.name,
                item.category,
                item.stock,
                item.price,
                item.barcode,
            ),
        )

        self.database.connection.commit()

    def get_all(self):

        self.database.cursor.execute(
            "SELECT item_id, name, category, stock, price, barcode FROM inventory"
    )

        rows = self.database.cursor.fetchall()

        items = []

        for row in rows:

            item = Item(
                item_id=row[0],
                name=row[1],
                category=row[2],
                stock=row[3],
                price=row[4],
                barcode=row[5],
            )

            items.append(item)

        return items

    def update(self, item):

        self.database.cursor.execute(
            """
            UPDATE inventory

            SET
                name = ?,
                category = ?,
                stock = ?,
                price = ?,
                barcode = ?

            WHERE item_id = ?
            """,
            (
                item.name,
                item.category,
                item.stock,
                item.price,
                item.barcode,
                item.item_id,
            ),
        )

        self.database.connection.commit()