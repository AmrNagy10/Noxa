import os
import main
import requests
from Commands import *
from colorama import Fore
from AiMassageManager import *
from telegram import Update
#from telegram.bot import Bot
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

Token = main.vars("TELEGRAM_BOT_TOKEN")
Documetspath = main.vars("NoxaDownloads")
async def main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    async def handle_message():
        Message = {
            "YouTubeSearch": lambda inputs: YoutubeSearch(inputs),
            "Goto": lambda inputs: Goto(inputs),
            "Site": lambda inputs: Site(inputs),
            "Getfrom": lambda inputs: Getfrom(inputs),
            "Ask": lambda inputs: Askai(inputs),
            "translate": lambda inputs: translte(inputs),
            "lock": lambda arg: os.system("gnome-screensaver-command -l"),
            "exit": lambda arg: exit("Exiting the program safely...")
        }
        if update.message.text:
            commands = Ai(message=update.message.text).Ai()
            for task in Message.keys():
                if commands[0].strip() == task:
                    dotask = Message.get(task)
                    if dotask:
                        await dotask(commands[1:])
                        break
        elif update.message.photo:
            photo_file = await update.message.photo[-1].get_file()
            await SaveImages(photo_file,Documetspath)
    await handle_message()


if __name__ == "__main__":
    application = ApplicationBuilder().token(Token).build()
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, main)
    application.add_handler(message_handler)
    photo_handler = MessageHandler(filters.PHOTO, main)
    application.add_handler(photo_handler)
    print(f"{Fore.BLUE}Noxa is Running... ")
    application.run_polling()
