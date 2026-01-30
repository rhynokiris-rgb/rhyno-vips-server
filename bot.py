import os
import json
from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# --- CONFIGURATION ---
TOKEN = "7724212557:AAG9z_T_G8U7lX1BvAovF4k7u9y0"
ADMIN_ID = 2097574959
DATA_FILE = "data.json"

# Flask setup taaki Render bot ko band na kare
app = Flask('')
@app.route('/')
def home():
    return "RHYNO BOTS is Online!"

def run_web_server():
    app.run(host='0.0.0.0', port=8080)

def main():
    # Flask ko dusre thread mein chalana
    Thread(target=run_web_server).start()

    # Telegram Bot setup
    application = Application.builder().token(TOKEN).build()
    
    # Simple start command handler
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("👋 Welcome to GNF PREMIUM MOD (Render Version)")

    application.add_handler(CommandHandler("start", start))
    
    print("Bot is starting on Cloud...")
    application.run_polling()

if __name__ == '__main__':
    main()
  
