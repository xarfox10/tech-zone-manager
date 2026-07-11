class ItemRepository:

    def __init__(self):
        self.items = []

    def save(self, item):
        self.items.append(item)

    def get_all(self):
        return self.items