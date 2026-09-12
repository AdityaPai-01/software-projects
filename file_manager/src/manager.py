from pathlib import Path


class File_Manager:
    def __init__(self):
        self.directory = []

    def change_directory(self, name):
        self.directory.append(Path(name))
        items = list(Path(name).iterdir())
        return items

    def previous_directory(self):
        pass