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

    def __init__(self):
        super().__init__()

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
            "name": self.name_input.text(),
            "category": self.category_input.text(),
            "stock": self.stock_input.text(),
            "price": self.price_input.text(),
            "barcode": self.barcode_input.text(),
    }

        self.item_saved.emit(item)

        self.accept()