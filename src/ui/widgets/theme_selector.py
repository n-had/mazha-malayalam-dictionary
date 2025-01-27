from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox
from PySide6.QtCore import Signal, Qt


class ThemeSelector(QWidget):
    theme_changed = Signal(str)  # Signal to notify when the theme changes

    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        
        self.theme_dropdown = QComboBox()
        self.theme_dropdown.setStyleSheet(
            """
            QComboBox {
                padding: 6px;
                font-size: 16px;
            }
            """
        )
        self.theme_dropdown.addItems(["തീം തിരഞ്ഞെടുക്കുക - Select a Theme", "Light", "Dark"])
        self.theme_dropdown.setItemData(0, 0, role=Qt.UserRole)

        self.theme_dropdown.currentTextChanged.connect(self.on_theme_change)
        
        layout.addWidget(self.theme_dropdown)
        self.setLayout(layout)

    def on_theme_change(self, theme: str):
        theme = theme.lower()
        self.theme_changed.emit(theme)
