import os
import logging
import webbrowser
from FileManager import FileManager
from telegram import Update
from telegram import Bot
from pytube import Search
from yt_dlp import YoutubeDL
from telegram.request import HTTPXRequest
from colorama import Fore
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

request = HTTPXRequest(media_write_timeout=120)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = Bot(token=TOKEN, request=request)
logging.basicConfig(
        filename="bot.log",
        format="%(levelname)s - %(message)s",
        level=logging.INFO
    )

async def main(update: Update, context: ContextTypes.DEFAULT_TYPE):

        async def YoutubeSearch(received_message):
            keyWord = received_message.replace("YouTubeSearch ", "")
            links = [v.watch_url for v in Search(keyWord).results[:4]]
            for id, link in enumerate(links,1):

                info = YoutubeDL({"quiet": True}).extract_info(link, download=False)
                title = info.get('title', 'N/A')
                views = info.get('view_count', 'N/A')
                ved_info = (
                    f"Video {id}:\n"
                    f"Title: {title}\n"
                    f"Views: {views:,}\n"
                    f"Link: {link}\n"
                )
                await context.bot.send_message(
                    chat_id=CHAT_ID,
                    text=ved_info
                )
            await context.bot.send_message(chat_id=CHAT_ID, text="Done")

        async def Goto(received_message):
            path = received_message.replace("Goto ", "")
            files = FileManager(path).getFiles()
            for Name in range(len(files)):
                await context.bot.send_message(
                    chat_id=CHAT_ID, text=f"{files[Name]}"
                )

        async def Getfrom(received_message):
            path = received_message.replace("Getfrom ", "").split(" ")
            name = FileManager(path[0]).getpath(' '.join(path[1:]))
            try:
                await context.bot.sendDocument(
                    chat_id=CHAT_ID,
                    document=name,
                    caption=f"This is {path[1]} from {path[0]} folder",
                    write_timeout=120,
                )
            except Exception as ex:
                await context.bot.send_message(
                    chat_id=CHAT_ID, text=f"I got {ex} Error :( "
                )

        async def Site(received_message):
            URL = received_message.replace("Site ", "")
            if "https://" not in URL:
                webbrowser.open(url=f"https://www.{URL}")
            else:
                webbrowser.open(url=URL)

        async def handle_message():
            received_message = str(update.message.text)
            Message = {
            "YouTubeSearch": lambda: YoutubeSearch(received_message),
            "Goto": lambda: Goto(received_message),
            "Getfrom": lambda: Getfrom(received_message),
            "Site": lambda: Site(received_message),
            "lock": lambda: os.system("gnome-screensaver-command -l")
            }
            for task in Message.keys():
                if received_message.startswith(task):
                    doTask = Message.get(task)
                    if doTask:
                        await doTask()

        await handle_message()

if __name__ == "__main__":
    application = (
        ApplicationBuilder()
        .token(TOKEN)
        .build()
    )
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, main)
    application.add_handler(message_handler)
    print(f"{Fore.BLUE}Noxa is Running... ")
    application.run_polling()
