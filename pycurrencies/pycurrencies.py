from typing import Optional
from typing_extensions import Annotated
from termcolor import colored
import typer

from pycurrencies.bitcoin_scrapper import BitcoinScrapper
from pycurrencies.dolar_scrapper import DolarScrapper

DOLAR_URL = "https://dolarhoy.com/"
BITCOIN_URL = "https://coinmarketcap.com/currencies/bitcoin/"


def dolar_price():
    dolar_scraper = DolarScrapper(DOLAR_URL)
    compra, venta = dolar_scraper.scrape_dolar_values()
    print(dolar_scraper.print_dolar_message(compra, venta))
    raise typer.Exit()

def bitcoin_price():
    bitcoin_scraper = BitcoinScrapper(BITCOIN_URL)
    compra, venta = bitcoin_scraper.scrape_bitcoin_values()
    print(bitcoin_scraper.print_bitcoin_price(compra, venta))
    raise typer.Exit()


def welcome_message() -> str:
    return f"""
        {colored("Bienvenido!", "yellow", "on_black", attrs=["bold"])}
        Este programa te permite obtener los valores actuales de varias monedas en Argentina
    """


def main(
    dolar: Annotated[
        Optional[bool],
        typer.Option(
            "--dolar", "-d", help="Obtener información del dólar", is_flag=True
        ),
    ] = None,
    bitcoin: Annotated[
        Optional[bool],
        typer.Option(
            "--bitcoin", "-b", help="Obtener información del bitcoin", is_flag=True
        ),
    ] = None
):
    print(welcome_message())
    if dolar is not None:
        dolar_price()
    else:
        print("No se seleccionó ninguna moneda")


if __name__ == "__main__":
    typer.run(main)
