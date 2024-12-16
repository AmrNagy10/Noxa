import os
import main
from Commands import *
from colorama import Fore
from AiMassageManager import *
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

Token = main.vars("TELEGRAM_BOT_TOKEN")
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
        commands = Ai(message=update.message.text).Ai()
        for task in Message.keys():
            if commands[0].strip() == task:
                dotask = Message.get(task)
                if dotask:
                    await dotask(commands[1:])
                    break

    await handle_message()


if __name__ == "__main__":
    application = ApplicationBuilder().token(Token).build()
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, main)
    application.add_handler(message_handler)
    print(f"{Fore.BLUE}Noxa is Running... ")
    application.run_polling()
