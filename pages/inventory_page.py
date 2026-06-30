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

        self.table = QTableWidget()

        self.table.setColumnCount(4)

        self.table.setHorizontalHeaderLabels([
            "Item",
         "Category",
         "Stock",
         "Price",
])

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
)

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

        row = self.table.rowCount()

        self.table.insertRow(row)

        self.table.setItem(row, 0, QTableWidgetItem(item["name"]))
        self.table.setItem(row, 1, QTableWidgetItem(item["category"]))
        self.table.setItem(row, 2, QTableWidgetItem(item["stock"]))
        self.table.setItem(row, 3, QTableWidgetItem(item["price"]))