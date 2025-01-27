from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QGroupBox,
    QScrollArea,
    QSizePolicy,
)
from PySide6.QtCore import Qt


class ResultWidget(QWidget):
    def __init__(self, status_bar):
        super().__init__()
        self.status_bar = status_bar

        # Create and configure the scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)  # Make the scroll area resize the widget

        # Create a container widget for the scroll area and set layout
        container_widget = QWidget()
        container_widget.setObjectName("resultContainer")
        self.layout = QVBoxLayout(container_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setAlignment(Qt.AlignTop)

        # Set the container widget as the scroll area's widget
        scroll_area.setWidget(container_widget)

        # Set the main layout of the ResultWidget
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

        self.type_mapping = {
            "{}": "",
            "{-}": "-",
            "{v}": "Verb - ക്രിയ",
            "{n}": "Noun - നാമം",
            "{a}": "Adjective - വിശേഷണം",
            "{idm}": "Idiom - ഭാഷാശൈലി",
            "{adv}": "Adverb - ക്രിയാവിശേഷണം",
            "{conj}": "Conjunction - അവ്യയം",
            "{prep}": "Preposition - ഉപസര്‍ഗം",
            "{phrv}": "Phrasal Verb - ഉപവാക്യ ക്രിയ",
            "{interj}": "Interjection - വ്യാക്ഷേപകം",
            "{pron}": "Pronoun - സര്‍വ്വനാമം",
            "{propn}": "Proper Noun - സംജ്ഞാനാമം",
            "{auxv}": "Auxiliary Verb - പൂരകകൃതി",
            "{sfx}": "Suffix - പ്രത്യയം",
            "{pfx}": "Prefix - പൂർവ്വപ്രത്യയം",
            "{abbr}": "Abbreviation - സംക്ഷേപം",
            "{phr}": "Phrase - വാക്യം",
        }

    def update_definitions(self, grouped_definitions):
        self.clear_previous_content()

        # Add new grouped definitions
        for type_, contents in grouped_definitions.items():
            type_name = self.get_type_name(type_)
            group_box = QGroupBox(f"{type_name}")
            group_box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
            group_layout = QVBoxLayout()
            for content in contents:
                definition_button = QPushButton(content)
                definition_button.clicked.connect(
                    lambda checked, text=content: self.copy_to_clipboard_and_notify(
                        text
                    )
                )
                definition_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                group_layout.addWidget(definition_button)

            group_box.setLayout(group_layout)
            self.layout.addWidget(group_box)

    def clear_previous_content(self):
        while self.layout.count():
            widget = self.layout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

    def get_type_name(self, type_code):
        return self.type_mapping.get(type_code, f"Type: {type_code[1:-1]}")

    def copy_to_clipboard_and_notify(self, text):
        QApplication.clipboard().setText(text)
        self.status_bar.showMessage(f"Copied '{text}' to clipboard", 2000)
