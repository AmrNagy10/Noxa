import os
from main import vars

class FileManager:
    def __init__(self, getFrom: str):
        if getFrom == "Downloads":
            self.path = vars("Downloads")
        elif getFrom == "Documents":
            self.path = vars("Documents")
        elif getFrom == "Pictures":
            self.path = vars("Pictures")
        elif getFrom == "Videos":
            self.path = vars("Videos")
        elif getFrom == "Music":
            self.path = vars("Music")
        elif getFrom == "Telegram":
            self.path = vars("Telegram")

    def getpath(self, file: str):
        for filename in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, filename)) and filename == file:
                return f"{self.path}/{filename}"

    def getFiles(self):
        file_names = []
        for filename in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, filename)):
                file_names.append(filename)
        return file_names
