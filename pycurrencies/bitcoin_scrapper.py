from bs4 import BeautifulSoup
import requests
from termcolor import colored


class BitcoinScrapper:
    """Bitcoin Scrapper class"""

    def __init__(self, url) -> None:
        self.ulr = url

    def scrape_bitcoin_values(self) -> int:
        page = requests.get(self.url, timeout=10)
        soup = BeautifulSoup(page.content, "html.parser")
        bitcoin_values = soup.find_all("div", class_="val")
        compra = int(bitcoin_values[0].get_text()[1:])
        venta = int(bitcoin_values[1].get_text()[1:])
        return compra, venta

    def print_bitcoin_price(self, compra: int, venta: int) -> str:
        print(
            f"""
            Gracias por utilizar este scrapper.
            Los valores actuales del bitcoin son:
            Compra: ${colored(compra, "green", "on_black")}
            Venta: ${colored(venta, "red", "on_black")}
        """
        )

    def send_bitcoin_price(self, number1: int, number2: int) -> str:
        return f"""
            Los valores actuales del bitcoin son:
            Compra: ${number1}
            Venta: ${number2}
        """
