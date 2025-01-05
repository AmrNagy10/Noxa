import os
import logging
from pathlib import Path
from dotenv import load_dotenv

logging.basicConfig(
    filename="bot.log", format="%(levelname)s - %(message)s", level=logging.INFO
)
load_dotenv()

def Getmainpath(folder):
    home_dir = Path.home()
    paths = [home_dir / "Downloads", home_dir / "Desktop", home_dir / "Documents", home_dir / "Documents", home_dir / "Downloads"/ "Telegram"]
    with open(".env", "r+") as file:
        if not any(folder in item for item in file.readlines()):
            file.writelines(f"Downloads = {str(paths[0])} \nDesktop = {paths[1]} \nDocuments = {paths[2]} \nPictures = {paths[3]} \nTelegram = {paths[4]}")
def vars(name):
    return os.getenv(f"{name}")

