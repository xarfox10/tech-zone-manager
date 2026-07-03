from models.item import Item


class ItemService:

    def __init__(self):
        self.next_id = 1
        self.items = []

    def generate_item_id(self):
        item_id = f"TZ-{self.next_id:06d}"
        self.next_id += 1
        return item_id

    def create_item(
        self,
        name,
        category,
        stock,
        price,
        barcode="",
    ):

        item = Item(
            item_id=self.generate_item_id(),
            name=name,
            category=category,
            stock=stock,
            price=price,
            barcode=barcode,
        )

        self.items.append(item)
        
        return item