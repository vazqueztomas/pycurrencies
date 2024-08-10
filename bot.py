import os
import telebot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_message(message):
    bot.reply_to(message, "Hola! Soy un bot que te permite obtener información sobre el dólar y el bitcoin en Argentina. Para obtener información sobre el dólar, escribe /dolar. Para obtener información sobre el bitcoin, escribe /bitcoin.")

@bot.message_handler(func=lambda msg:True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
