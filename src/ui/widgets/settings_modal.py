from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QDialog,
    QDialogButtonBox,
)
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices, QIcon
from ui.widgets.theme_selector import ThemeSelector
from utils import resource_path

class SettingsModal(QDialog):
    def __init__(self, apply_theme, parent=None):
        super().__init__(parent)
        
        # Set up the modal window properties
        self.setWindowTitle("Settings")
        self.setWindowIcon(QIcon(resource_path("src/assets/ma.ico")))
        self.setModal(True)
        self.apply_theme = apply_theme

        self.layout = QVBoxLayout(self)

        theme_selector = ThemeSelector()
        theme_selector.theme_changed.connect(self.apply_theme)

        self.layout.addWidget(theme_selector)

        info_container = QWidget()
        info_container.setObjectName("info_container")
        info_container_layout = QVBoxLayout(info_container)

        about = QLabel(
            'Based on the <a href="https://olam.in" style="text-decoration: none;">Olam - ഓളം</a> open-source dictionary.',
            self,
        )
        about.setWordWrap(True)
        about.linkActivated.connect(self.open_link)

        info_container_layout.addWidget(about)
        creator = QLabel(
            'Made with 💖 by <a href="https://github.com/n-had" style="text-decoration: none;">Nihad</a>',
            self,
        )
        creator.setWordWrap(True)
        creator.linkActivated.connect(self.open_link)
        info_container_layout.addWidget(creator)
        
        version = QLabel("v0.1.0", self)
        version.setWordWrap(True)
        info_container_layout.addWidget(version)
        self.layout.addWidget(info_container)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok, self)
        button_box.setStyleSheet("padding: 6px 25px;font-size: 14px;")
        ok_button = button_box.button(QDialogButtonBox.Ok)
        ok_button.setText("Close")

        button_box.accepted.connect(self.accept)
        self.layout.addWidget(button_box)

        self.setFixedSize(460, 250)
        self.setStyleSheet(
            """
            QLabel {
                font-size: 17px;
            }
        """
        )

    # Slot to handle the link click and open in the browser
    def open_link(self, url):
        QDesktopServices.openUrl(QUrl(url))  # Open the URL in the default browser
