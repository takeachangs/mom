import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hi {update.message.chat.first_name}, how has your day been?")

if __name__ == '__main__':
    application = ApplicationBuilder().token('7180141681:AAFF_flKymO-nrw96n1UvfMpnPpXy433Erk').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()