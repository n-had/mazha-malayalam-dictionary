from PySide6.QtWidgets import QStatusBar, QPushButton
from ui.widgets.settings_modal import SettingsModal


class StatusBarWidget(QStatusBar):
    def __init__(self, apply_theme, parent=None):
        super().__init__(parent)
        self.apply_theme = apply_theme
        self.settings_button = QPushButton(" ⛭ Settings")
        self.settings_button.setObjectName("settings_button")
        self.settings_button.clicked.connect(self.show_settings_modal)
        self.addWidget(self.settings_button)

    def show_settings_modal(self):
        settings_modal = SettingsModal(self.apply_theme)
        settings_modal.exec()
