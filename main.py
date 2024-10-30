import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import openai
from dotenv import load_dotenv
from bot import PalmeirasBot

if __name__ == '__main__':
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")

    openai.api_key = openai_api_key
    bot = PalmeirasBot()

    application = ApplicationBuilder().token(telegram_token).build()
    
    start_handler = CommandHandler('start', bot.start)
    application.add_handler(start_handler)
    
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, bot.handle_message)
    application.add_handler(message_handler)
    
    # Inicia o bot
    application.run_polling()
