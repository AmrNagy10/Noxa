import os

Downloads = "/home/amr-nagy/Downloads"
Documents = "/home/amr-nagy/Documents"
Pictures = "/home/amr-nagy/Pictures"
Telegram = "/home/amr-nagy/Downloads/Telegram Desktop"
Videos = "/home/amr-nagy/Videos"
Music = "/home/amr-nagy/Music"


class FileManager:
    def __init__(self, getFrom: str):
        if getFrom == "Downloads":
            self.path = Downloads
        elif getFrom == "Documents":
            self.path = Documents
        elif getFrom == "Pictures":
            self.path = Pictures
        elif getFrom == "Videos":
            self.path = Videos
        elif getFrom == "Music":
            self.path = Music
        elif getFrom == "Telegram":
            self.path = Telegram

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
