from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)
from PySide6.QtCore import Qt


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("Dashboard")
        title.setStyleSheet(
            """
            font-size: 24px;
            font-weight: bold;
            padding: 10px;
            """
        )

        welcome = QLabel(
            "Welcome back to TECH ZONE Manager!"
        )

        welcome.setAlignment(Qt.AlignTop)

        layout.addWidget(title)
        layout.addWidget(welcome)
        layout.addStretch()

        self.setLayout(layout)