from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon
from ui.widgets.input_widget import InputWidget
from ui.widgets.result_widget import ResultWidget
from ui.widgets.status_bar_widget import StatusBarWidget
from utils import get_system_theme, load_stylesheet, resource_path


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window properties
        self.setWindowTitle("Mazha Malayalam Dictionary")
        self.setWindowIcon(QIcon(resource_path("src/assets/ma.ico")))
        self.setGeometry(100, 100, 512, 680)

        # Set up the central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setObjectName("centralWidget")
        system_theme = get_system_theme()
        self.apply_theme(theme=system_theme)

        # Create the layout and add the widgets
        self.layout = QVBoxLayout(self.central_widget)
        self.status_bar = StatusBarWidget(self.apply_theme)
        self.input_widget = InputWidget()
        self.result_widget = ResultWidget(self.status_bar)
        self.layout.addWidget(self.input_widget)
        self.layout.addWidget(self.result_widget)

        # Connect the signal from InputWidget to update the ResultWidget
        self.input_widget.word_selected.connect(self.update_definition)
        self.setStatusBar(self.status_bar)

    def update_definition(self, word):
        definitions = self.input_widget.dictionary_data.get_definition(word)
        # Group definitions by type (noun, verb, etc.)
        grouped_definitions = {}
        # print(definitions)
        for type_, content in definitions:
            if type_ not in grouped_definitions:
                grouped_definitions[type_] = []
            grouped_definitions[type_].append(content)

        self.result_widget.update_definitions(grouped_definitions)

    def apply_theme(self, theme: str):
        if theme == "light":
            stylesheet = load_stylesheet(resource_path("src/assets/light_styles.qss"))
            self.setStyleSheet("")
            self.setStyleSheet(stylesheet)
        elif theme == "dark":
            stylesheet = load_stylesheet(resource_path("src/assets/dark_styles.qss"))
            self.setStyleSheet("")
            self.setStyleSheet(stylesheet)
        elif theme == "system":
            system_theme = get_system_theme()
            self.setStyleSheet("")
            self.apply_theme(system_theme)
