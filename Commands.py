import os
import webbrowser
import requests
from sender import Sender
from pytube import Search
from yt_dlp import YoutubeDL
from AiMassageManager import *
from FileManager import FileManager
from deep_translator import GoogleTranslator


async def translte(inputs: list):
    translator = GoogleTranslator(source="auto", target=inputs[-1])
    result = translator.translate(inputs[0])
    await Sender(massage=result).send_message()


async def Site(URL):
    if "https://" not in URL:
        webbrowser.open(url=URL[0])
    else:
        webbrowser.open(url=URL[0])
    await Sender(massage="Opened").send_message()


async def YoutubeSearch(Keyword):
    links = [v.watch_url for v in Search(Keyword).results[:4]]
    for ID, link in enumerate(links, 1):
        info = YoutubeDL({"quiet": True}).extract_info(link, download=False)
        title = info.get("title", "N/A")
        views = info.get("view_count", "N/A")
        ved_info = (
            f"Video {ID}:\n" f"Title: {title}\n" f"Views: {views:,}\n" f"Link: {link}\n"
        )
        await Sender(massage=ved_info).send_message()
    await Sender(massage="End").send_message()


async def Goto(Fname):
    files = FileManager(Fname[0]).getFiles()
    for Name in range(len(files)):
        await Sender(massage=f"{files[Name]}").send_message()


async def Getfrom(path):
    name = FileManager(path[1]).getpath(path[0])
    try:
        await Sender(massage=f"This is {path[1]} from {path[0]} folder").send_document(
            document=name
        )
    except Exception as ex:
        await Sender(massage=f"I got {ex} Error :( ").send_message()


async def Askai(message):
    responce = Ai(message).speakwithai()
    await Sender(massage=responce).send_message()

async def SaveImages(photo_file, Savepath):
    filename = photo_file.file_path.split('/')
    save_path = os.path.join(Savepath, filename[-1])
    with open(save_path, 'wb') as file:
        file.write(requests.get(photo_file.file_path).content)
    await Sender(massage=f"Photo downloaded successfully at: {save_path}").send_message()