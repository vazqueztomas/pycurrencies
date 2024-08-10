import telebot
from dotenv import load_dotenv

from pycurrencies.bitcoin_scrapper import BitcoinScrapper
from pycurrencies.dolar_scrapper import DolarScrapper

from .utils import dolar_url, bitcoin_url, BOT_TOKEN

load_dotenv()

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_message(message):
    bot.reply_to(
        message,
        "Hola! Soy un bot que te permite obtener información sobre el dólar y el bitcoin en Argentina. Para obtener información sobre el dólar, escribe /dolar. Para obtener información sobre el bitcoin, escribe /bitcoin.",
    )


@bot.message_handler(commands=["dolar"])
def dolar_price(message):
    dolar_scraper = DolarScrapper(dolar_url)
    compra, venta = dolar_scraper.scrape_dolar_values()
    bot.reply_to(message, dolar_scraper.print_dolar_message(compra, venta))


@bot.message_handler(commands=["bitcoin"])
def bitcoin_price(message):
    bitcoin_scraper = BitcoinScrapper(bitcoin_url)
    compra, venta = bitcoin_scraper.scrape_bitcoin_values()
    bot.reply_to(message, bitcoin_scraper.print_bitcoin_price(compra, venta))


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
