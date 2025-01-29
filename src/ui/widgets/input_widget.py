from PySide6.QtWidgets import QWidget, QLineEdit, QListWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, Signal
from data.dictionary_data import DictionaryData


class InputWidget(QWidget):
    word_selected = Signal(str)  # Signal to notify when a word is selected

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        app_title = QLabel("മഴ", self)
        app_title.setObjectName("appTitle")
        app_title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(app_title)

        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText("english word / മലയാള പദം")

        self.suggestions_list = QListWidget(self)

        self.layout.addWidget(self.input_box)
        self.layout.addWidget(self.suggestions_list)

        self.suggestions_list.hide()

        self.input_box.textChanged.connect(self.on_text_changed)
        self.suggestions_list.itemClicked.connect(self.on_suggestion_clicked)

        # Initialize the dictionary data
        self.dictionary_data = DictionaryData()

    def on_text_changed(self, text):
        self.suggestions_list.clear()
        if text.strip():
            suggestions = self.dictionary_data.get_suggestions(text)
            if suggestions:
                self.suggestions_list.clear()
                self.suggestions_list.show()
                self.suggestions_list.addItems(suggestions)
                self.suggestions_list.setCurrentRow(0)
            else:
                self.suggestions_list.hide()
        else:
            self.suggestions_list.clear()
            self.suggestions_list.hide()

    def on_suggestion_clicked(self, item):
        selected_word = item.text()
        self.input_box.setText(selected_word)
        self.word_selected.emit(selected_word)  # Emit the selected word
        self.suggestions_list.hide()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            current_row = self.suggestions_list.currentRow()
            if current_row > 0:
                self.suggestions_list.setCurrentRow(current_row - 1)
        elif event.key() == Qt.Key_Down:
            current_row = self.suggestions_list.currentRow()
            if current_row < self.suggestions_list.count() - 1:
                self.suggestions_list.setCurrentRow(current_row + 1)
        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if self.suggestions_list.currentRow() >= 0:
                self.on_suggestion_clicked(self.suggestions_list.currentItem())
                self.suggestions_list.hide()
        else:
            super().keyPressEvent(event)  # Call the base class implementation
