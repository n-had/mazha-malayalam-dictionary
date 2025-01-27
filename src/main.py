import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont, QFontDatabase, QIcon
from ui.main_window import MainWindow
from utils import resource_path

from PySide6.QtGui import QColor, QPalette
from PySide6.QtCore import Qt


if __name__ == "__main__":
    app = QApplication(sys.argv + ["-platform", "windows:darkmode=2"])
    app.setWindowIcon(QIcon(resource_path("src/assets/dict.ico")))
    app.setStyle("Fusion")
    font_path = resource_path("src/assets/Manjari-Regular.ttf")
    font_id = QFontDatabase.addApplicationFont(font_path)
    if font_id == -1:
        print("Failed to load the custom font.")
    else:
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        custom_font = QFont(font_family, 8)
        app.setFont(custom_font)

    palette = QPalette()
    accent_color = QColor(20, 144, 223)
    palette.setColor(QPalette.Highlight, accent_color)
    palette.setColor(QPalette.Link, accent_color)
    app.setPalette(palette)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
