import os
import logging
from pathlib import Path
from dotenv import load_dotenv

logging.basicConfig(
    filename="bot.log", format="%(levelname)s - %(message)s", level=logging.INFO
)
load_dotenv()
home_dir = Path.home()
def check_folder_existed():
    if not os.path.exists(home_dir / "Documents" / "Noxa" /"NoxaDownloads"):
        os.makedirs(home_dir / "Documents"/ "Noxa" /"NoxaDownloads")

def Getmainpath(folder):
    check_folder_existed()
    paths = [
        home_dir / "Downloads",
        home_dir / "Desktop",
        home_dir / "Documents",
        home_dir / "Pictures",
        home_dir / "Downloads" / "Telegram",
        home_dir / "Documents" / "Noxa" / "NoxaDownloads"
    ]
    with open(".env", "r+") as file:
        lines = file.readlines()
        if not any(folder in line for line in lines):
            file.writelines([
                f"Downloads = {paths[0]}\n",
                f"Desktop = {paths[1]}\n",
                f"Documents = {paths[2]}\n",
                f"Pictures = {paths[3]}\n",
                f"Telegram = {paths[4]}\n",
                f"NoxaDownloads = {paths[5]}\n"
            ])
        file.truncate()

def vars(name):
    value = os.getenv(name)
    if value is not None:
        return value
    else:
        Getmainpath(name)
        return None
