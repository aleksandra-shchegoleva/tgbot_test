from telegram import Update
from telegram.ext import CommandHandler, Application
from dotenv import load_dotenv
import os

load_dotenv()

async def start(update, context):
    await update.message.reply_text("Привет!")

if __name__ == "__main__":
    token = os.getenv("TOKEN")
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler('start', start))
    app.run_polling()
    print("Бот запущен!")