from telegram.ext import filters, ApplicationBuilder, CommandHandler, MessageHandler
from telegram_handler import TelegramInstance


def main():
    telegram = TelegramInstance()

    application = ApplicationBuilder().token('7180141681:AAFF_flKymO-nrw96n1UvfMpnPpXy433Erk').build()
    
    start_handler = CommandHandler('start', telegram.start)
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), telegram.chat)

    application.add_handler(start_handler)
    application.add_handler(message_handler)
    
    application.run_polling()

main()