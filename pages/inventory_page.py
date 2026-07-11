from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView,
)

from dialogs.item_dialog import ItemDialog
from services.item_service import ItemService

class InventoryPage(QWidget):

    def __init__(self):
        super().__init__()
        self.item_service = ItemService()

        layout = QVBoxLayout()

        title = QLabel("Inventory")

        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            padding:10px;
        """)

        top_bar = QHBoxLayout()

        add_button = QPushButton("+ New Item")
        add_button.clicked.connect(self.open_item_dialog)

        search_box = QLineEdit()
        search_box.setPlaceholderText("Search item...")

        top_bar.addWidget(add_button)
        top_bar.addStretch()
        top_bar.addWidget(search_box)

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "Item ID",
            "Item",
            "Category",
            "Stock",
            "Price",
])

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
)
        self.table.cellDoubleClicked.connect(self.edit_item)
        
        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(
            QAbstractItemView.NoEditTriggers
)
        self.table.setSelectionBehavior(
            QAbstractItemView.SelectRows
)

        layout.addWidget(title)
        layout.addLayout(top_bar)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def open_item_dialog(self):

        dialog = ItemDialog()

        dialog.item_saved.connect(self.add_item_to_table)

        dialog.exec()

    def add_item_to_table(self, item):

        item = self.item_service.create_item(
            name=item["name"],
            category=item["category"],
            stock=item["stock"],
            price=item["price"],
            barcode=item["barcode"],
)
        print(item.item_id)

        row = self.table.rowCount()

        self.table.insertRow(row)

        self.table.setItem(row, 0, QTableWidgetItem(item.item_id))
        self.table.setItem(row, 1, QTableWidgetItem(item.name))
        self.table.setItem(row, 2, QTableWidgetItem(item.category))
        self.table.setItem(row, 3, QTableWidgetItem(str(item.stock)))
        self.table.setItem(row, 4, QTableWidgetItem(str(item.price)))

        print("Items inside ItemService:")

        for item in self.item_service.get_all_items():
            print(item.item_id, "-", item.name)

    def update_item(self, item):

        row = self.sender().row

        self.table.setItem(row, 0, QTableWidgetItem(item["name"]))
        self.table.setItem(row, 1, QTableWidgetItem(item["category"]))
        self.table.setItem(row, 2, QTableWidgetItem(item["stock"]))
        self.table.setItem(row, 3, QTableWidgetItem(item["price"]))

    def edit_item(self, row, column):
        item = {
            "name": self.table.item(row, 0).text(),
            "category": self.table.item(row, 1).text(),
            "stock": self.table.item(row, 2).text(),
            "price": self.table.item(row, 3).text(),
            "barcode": "",
}

        dialog = ItemDialog(item, row)

        dialog.item_saved.connect(self.update_item)

        dialog.exec()
    