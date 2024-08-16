import requests
from termcolor import colored


class BitcoinScrapper:
    """Bitcoin Scrapper class"""

    def __init__(self, url) -> None:
        self.url = url

    def scrape_bitcoin_values(self) -> int | str | None:
        try:
            page = requests.get(self.url)
            price = page.json()["bpi"]["USD"]["rate"]
        except (requests.exceptions.RequestException, KeyError):
            return None
        return price

    def print_bitcoin_price(self, compra: int, venta: int) -> str:
        print(
            f"""
            Gracias por utilizar este scrapper.
            Los valores actuales del bitcoin son:
            Compra: ${colored(compra, "green", "on_black")}
            Venta: ${colored(venta, "red", "on_black")}
        """
        )

    def send_bitcoin_price(self, price) -> str:
        return f"""
            El valor actual de Bitcoin es de {price} USD.
        """
