from repositories.item_repository import ItemRepository
from models.item import Item
from engine.id_engine import IdEngine

class ItemService:

    def __init__(self):
        self.repository = ItemRepository()
        self.id_engine = IdEngine()

    def create_item(
        self,
        name,
        category,
        stock,
        price,
        barcode="",
    ):

        item = Item(
            item_id=self.id_engine.generate("TZ"),
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

        self.repository.update(item)
        
        return item

    def item_exists(self, item_id):
        return self.get_item_by_id(item_id) is not None