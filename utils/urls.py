import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
dolar_url = os.getenv("DOLAR_URL")
bitcoin_url = os.getenv("BITCOIN_URL")
