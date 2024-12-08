import os
import logging
import webbrowser
from colorama import Fore
from pytube import Search
from yt_dlp import YoutubeDL
from telegram import Update, Bot
from FileManager import FileManager
from telegram.request import HTTPXRequest
from deep_translator import GoogleTranslator
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

request = HTTPXRequest(media_write_timeout=120)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = Bot(token=TOKEN, request=request)
logging.basicConfig(
    filename="bot.log", format="%(levelname)s - %(message)s", level=logging.INFO
)


async def main(update: Update, context: ContextTypes.DEFAULT_TYPE):

    async def send_message(massage):
        await context.bot.send_message(chat_id=CHAT_ID,text=massage)

    async def YoutubeSearch(received_message):
        Keyword = received_message.replace("YouTubeSearch ", "")
        links = [v.watch_url for v in Search(Keyword).results[:4]]
        for ID, link in enumerate(links, 1):
            info = YoutubeDL({"quiet": True}).extract_info(link, download=False)
            title = info.get("title", "N/A")
            views = info.get("view_count", "N/A")
            ved_info = (
                f"Video {ID}:\n"
                f"Title: {title}\n"
                f"Views: {views:,}\n"
                f"Link: {link}\n"
            )
            await send_message(massage=ved_info)
        await send_message(massage="Done")

    async def Goto(received_message):
        path = received_message.replace("Goto ", "")
        files = FileManager(path).getFiles()
        for Name in range(len(files)):
            await send_message(massage=f"{files[Name]}")

    async def Getfrom(received_message):
        path = received_message.replace("Getfrom ", "").split(" ")
        name = FileManager(path[0]).getpath(" ".join(path[1:]))
        try:
            await context.bot.sendDocument(
                chat_id=CHAT_ID,
                document=name,
                caption=f"This is {path[1]} from {path[0]} folder",
                write_timeout=120,
            )
        except Exception as ex:
            await send_message(
                massage=f"I got {ex} Error :( "
            )

    async def Site(received_message):
        URL = received_message.replace("Site ", "")
        if "https://" not in URL:
            webbrowser.open(url=f"https://www.{URL}")
        else:
            webbrowser.open(url=URL)
        await send_message("Open")

    async def translte(received_message):
        text = received_message.replace("translate ", "").split(" ")
        translator = GoogleTranslator(source="auto", target=text[-1])
        result = translator.translate(" ".join(text[:-1]))
        await send_message(massage=result)

    async def handle_message():
        received_message = str(update.message.text)
        Message = {
            "YouTubeSearch": lambda: YoutubeSearch(received_message),
            "Goto": lambda: Goto(received_message),
            "Getfrom": lambda: Getfrom(received_message),
            "Site": lambda: Site(received_message),
            "translate": lambda: translte(received_message),
            "lock": lambda: os.system("gnome-screensaver-command -l"),
        }
        for task in Message.keys():
            if received_message.startswith(task):
                doTask = Message.get(task)
                if doTask:
                    await doTask()

    await handle_message()


if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, main)
    application.add_handler(message_handler)
    print(f"{Fore.BLUE}Noxa is Running... ")
    application.run_polling()
