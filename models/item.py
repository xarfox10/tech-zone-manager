class Item:

    def __init__(
        self,
        item_id,
        name,
        category,
        stock,
        price,
        barcode="",
    ):

        self.item_id = item_id
        self.name = name
        self.category = category
        self.stock = stock
        self.price = price
        self.barcode = barcode