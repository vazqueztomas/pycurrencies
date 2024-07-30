from typing import Optional
from typing_extensions import Annotated
from termcolor import colored
import typer

from pycurrencies.dolar_scrapper import DolarScrapper

URL = "https://dolarhoy.com/"


def dolar_price():
    scraper = DolarScrapper(URL)
    compra, venta = scraper.scrape_dolar_values()
    print(scraper.print_dolar_message(compra, venta))
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
