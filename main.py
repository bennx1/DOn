# main.py
from keep_alive import keep_alive
import telebot
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")  # ambil token dari env var
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot aktif! Siap ngebut 💸")

# Jalankan server Flask agar bisa diping
keep_alive()

print("Bot siap... polling...")
bot.infinity_polling()