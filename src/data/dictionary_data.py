import csv, sys, os


class DictionaryData:
    def __init__(self):
        self.enml_data = {}
        self.datuk_data = {}
        self.enml_file_path = self.resource_path("src/data/enml.tsv")
        self.datuk_file_path = self.resource_path("src/data/datuk.tsv")
        self.load_data()

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.normpath(os.path.join(base_path, relative_path))

    def load_data(self):

        with open(self.enml_file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter="\t")
            next(reader)  # Skip the first row (header)
            for row in reader:
                # TODO: remove this check
                if len(row) == 3:
                    from_content, word_type, to_content = row
                    if from_content not in self.enml_data:
                        self.enml_data[from_content] = []
                    self.enml_data[from_content].append((word_type, to_content))

        with open(self.datuk_file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter="\t")
            next(reader)  # Skip the first row (header)
            for row in reader:
                # TODO: remove this check
                if len(row) == 3:
                    from_content, word_type, to_content = row
                    if from_content not in self.datuk_data:
                        self.datuk_data[from_content] = []
                    self.datuk_data[from_content].append((word_type, to_content))

    def get_suggestions(self, text):
        is_malayalam_text = self.is_malayalam(text)
        data_source = self.datuk_data if is_malayalam_text else self.enml_data
        if is_malayalam_text:
            return [word for word in data_source.keys() if word.startswith(text)][:30]
        else:
            return [
                word
                for word in data_source.keys()
                if word.lower().startswith(text.lower())
            ][:30]

    def get_definition(self, word):
        is_malayalam_text = self.is_malayalam(word)
        data_source = self.datuk_data if is_malayalam_text else self.enml_data
        entry = data_source.get(word)
        if entry:
            return entry
        return "Definition not found."

    def is_malayalam(self, text):
        for char in text:
            if char.isdigit() or char in [
                " ",
                '"',
                "(",
                ")",
                ",",
                "-",
                ".",
                ":",
                "<",
                "\u00ad",
            ]:
                continue
            if ord(char) < 0x0D00 or ord(char) > 0x0D7F:
                return False
        return True
