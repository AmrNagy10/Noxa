import main
from telegram import Bot


class Sender:
    def __init__(self, massage):
        self.chat_id = main.vars("CHAT_ID")
        self.massage = massage
        self.bot = Bot(token=main.vars("TELEGRAM_BOT_TOKEN"))

    async def send_message(self):
        await self.bot.send_message(chat_id=self.chat_id, text=self.massage)

    async def send_document(self, document):
        await self.bot.sendDocument(
            chat_id=self.chat_id,
            document=document,
            caption=self.massage,
            write_timeout=120,
        )
