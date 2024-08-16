from unittest.mock import Mock
import pytest
from pycurrencies.scrapers.dolar_scrapper import DolarScrapper
import requests


@pytest.fixture
def scrapper():
    url = "https://www.test.com"
    return DolarScrapper(url)


def test_scrape_dolar_values_success(mocker, scrapper):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = """
    <div class="val">$100</div>
    <div class="val">$200</div>
    """
    mocker.patch(
        "pycurrencies.scrapers.dolar_scrapper.requests.get", return_value=mock_response
    )

    compra, venta = scrapper.scrape_dolar_values()
    assert compra == 100
    assert venta == 200


def test_scrape_dolar_values_failure(mocker, scrapper):
    mocker.patch(
        "pycurrencies.scrapers.dolar_scrapper.requests.get",
        side_effect=requests.ConnectionError,
    )
    compra, venta = scrapper.scrape_dolar_values()
    assert compra is None
    assert venta is None


def test_print_dolar_message(scrapper):
    number1 = 100
    number2 = 200
    message = scrapper.print_dolar_message(number1, number2)
    assert "Compra: $100" in message
    assert "Venta: $200" in message
