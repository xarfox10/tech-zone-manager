from database.database import Database
from repositories.item_repository import ItemRepository
from models.item import Item

class ItemService:

    def __init__(self):
        self.next_id = 1
        self.repository = ItemRepository()
        self.database = Database()

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

        self.repository.save(item)
        
        return item
    
    def get_all_items(self):
        return self.repository.get_all()
    
    def get_item_by_id(self, item_id):
        for item in self.repository.get_all():
            if item.item_id == item_id:
                return item

        return None
    
    def update_item(
    self,
    item_id,
    name,
    category,
    stock,
    price,
    barcode,
):

        item = self.get_item_by_id(item_id)

        if item is None:
            return None

        item.name = name
        item.category = category
        item.stock = stock
        item.price = price
        item.barcode = barcode

        return item

    def item_exists(self, item_id):
        return self.get_item_by_id(item_id) is not None