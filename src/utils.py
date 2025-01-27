import sys, os, platform
from PySide6.QtCore import QFile, QTextStream


def resource_path(relative_path):
    """Get the absolute path to the resource, works for both dev and PyInstaller."""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.normpath(os.path.join(base_path, relative_path))


def load_stylesheet(file_path):
    file = QFile(file_path)
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    return stream.readAll()


def get_system_theme():
    if platform.system() == "Windows":
        from PySide6.QtCore import QSettings

        settings = QSettings(
            "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize",
            QSettings.NativeFormat,
        )
        return "dark" if settings.value("AppsUseLightTheme") == 0 else "light"
    elif platform.system() == "Darwin":
        import subprocess

        result = subprocess.run(
            ["defaults", "read", "-g", "AppleInterfaceStyle"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return "dark" if result.stdout.strip() == "Dark" else "light"
    else:
        return "dark"
