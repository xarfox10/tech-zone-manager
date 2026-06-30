from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
    QTableWidget,
)

from dialogs.item_dialog import ItemDialog

class InventoryPage(QWidget):

    def __init__(self):
        super().__init__()

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

        table = QTableWidget()

        table.setColumnCount(4)

        table.setHorizontalHeaderLabels(
            [
                "Item",
                "Category",
                "Stock",
                "Price",
            ]
        )

        layout.addWidget(title)
        layout.addLayout(top_bar)
        layout.addWidget(table)

        self.setLayout(layout)

    def open_item_dialog(self):

        dialog = ItemDialog()

        dialog.exec()