from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)
class ItemDialog(QDialog):

    item_saved = Signal(dict)

    def __init__(self, item=None, row=None):
        super().__init__()
        
        self.item = item
        self.row = row

        self.setWindowTitle("New Item")

        self.setFixedWidth(400)

        layout = QVBoxLayout()


        # Item Name
        layout.addWidget(QLabel("Item Name"))

        self.name_input = QLineEdit()

        layout.addWidget(self.name_input)

        # Category
        layout.addWidget(QLabel("Category"))

        self.category_input = QLineEdit()

        layout.addWidget(self.category_input)

        # Stock
        layout.addWidget(QLabel("Stock"))

        self.stock_input = QLineEdit()

        layout.addWidget(self.stock_input)

        # Price
        layout.addWidget(QLabel("Price"))

        self.price_input = QLineEdit()

        layout.addWidget(self.price_input)

        # Barcode
        layout.addWidget(QLabel("Barcode"))

        self.barcode_input = QLineEdit()

        layout.addWidget(self.barcode_input)

        if item:
            self.setWindowTitle("Edit Item")

            self.name_input.setText(item["name"])
            self.category_input.setText(item["category"])
            self.stock_input.setText(item["stock"])
            self.price_input.setText(item["price"])
            self.barcode_input.setText(item["barcode"])

        button_layout = QHBoxLayout()

        self.save_button = QPushButton("Save")

        self.save_button.clicked.connect(self.save_item)

        self.cancel_button = QPushButton("Cancel")

        button_layout.addStretch()

        button_layout.addWidget(self.save_button)

        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.cancel_button.clicked.connect(self.close)
    
    def save_item(self):

        item = {
            "item_id": self.item["item_id"] if self.item else "",
            "name": self.name_input.text(),
            "category": self.category_input.text(),
            "stock": self.stock_input.text(),
            "price": self.price_input.text(),
            "barcode": self.barcode_input.text(),
    }

        self.item_saved.emit(item)

        self.accept()