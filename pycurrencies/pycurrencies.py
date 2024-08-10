from typing import Optional
from typing_extensions import Annotated
from termcolor import colored
import typer
import os

from pycurrencies.bitcoin_scrapper import BitcoinScrapper
from pycurrencies.dolar_scrapper import DolarScrapper
from dotenv import load_dotenv

load_dotenv()

dolar_url = os.getenv("DOLAR_URL")
bitcoin_url = os.getenv("BITCOIN_URL")


def dolar_price():
    dolar_scraper = DolarScrapper(dolar_url)
    compra, venta = dolar_scraper.scrape_dolar_values()
    print(dolar_scraper.print_dolar_message(compra, venta))
    raise typer.Exit()


def bitcoin_price():
    bitcoin_scraper = BitcoinScrapper(bitcoin_url)
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
):
    print(welcome_message())
    if dolar is not None:
        dolar_price()
    else:
        print("No se seleccionó ninguna moneda")


if __name__ == "__main__":
    typer.run(main)
