import os
import logging
from dotenv import load_dotenv

logging.basicConfig(
    filename="bot.log", format="%(levelname)s - %(message)s", level=logging.INFO
)
load_dotenv()


def vars(name):
    return os.getenv(f"{name}")

