from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QMainWindow,
    QHBoxLayout,
    QWidget,
    QVBoxLayout,
    QStackedWidget,
)

from pages.dashboard_page import DashboardPage
from pages.inventory_page import InventoryPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("TECH ZONE Manager")
        self.resize(1200, 700)

        self.build_ui()

    def build_ui(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Sidebar
        sidebar = QVBoxLayout()

        pages = [
            "Dashboard",
            "POS",
            "Inventory",
            "Customers",
            "Suppliers",
            "Repairs",
            "Reports",
            "Settings",
        ]

        for page in pages:
            button = QPushButton(page)
            button.setMinimumHeight(45)

            button.clicked.connect(
                lambda checked=False, p=page: self.change_page(p)
            )

            sidebar.addWidget(button)

        sidebar.addStretch()

        sidebar_widget = QWidget()
        sidebar_widget.setLayout(sidebar)
        sidebar_widget.setFixedWidth(220)

        # Content
        # Pages
        self.stack = QStackedWidget()

        self.dashboard_page = DashboardPage()
        self.inventory_page = InventoryPage()

        self.stack.addWidget(self.dashboard_page)
        self.stack.addWidget(self.inventory_page)

        # Add to main layout
        main_layout.addWidget(sidebar_widget)
        main_layout.addWidget(self.stack)

    def change_page(self, page):

        if page == "Dashboard":
            self.stack.setCurrentWidget(
                self.dashboard_page
        )

        elif page == "Inventory":
            self.stack.setCurrentWidget(
                self.inventory_page
        )