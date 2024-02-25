import logging
from telegram import Update
from telegram.ext import ContextTypes
from cohere_chat import CohereChat

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class TelegramInstance:
    user_id: int
    user_name: str
    cohere_bot: CohereChat

    def __init__(self) -> None:
        self.user_id = None
        self.user_name = None
        self.cohere_bot = None

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.user_id = update.message.from_user.id
        self.user_name = update.message.from_user.name
        self.cohere_bot = CohereChat(0.2, update.message.from_user.name)

        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hi {update.message.chat.first_name}, how has your day been?")

    async def chat(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        response = self.cohere_bot.get_response(update.message.text)
        message: str = response.text
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)