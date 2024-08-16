import pytest
from unittest.mock import Mock
import requests
from pycurrencies import BitcoinScrapper


@pytest.fixture
def scrapper():
    url = "https://test.com"
    return BitcoinScrapper(url)


def test_scrape_bitcoin_values_success(mocker, scrapper):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"bpi": {"USD": {"rate": "50000"}}}
    mocker.patch("requests.get", return_value=mock_response)

    price = scrapper.scrape_bitcoin_values()
    assert price == "50000"


def test_scrape_bitcoin_values_failure(mocker, scrapper):
    mocker.patch("requests.get", side_effect=requests.ConnectionError)
    price = scrapper.scrape_bitcoin_values()
    assert price is None


def test_print_bitcoin_price(capsys, scrapper):
    compra = 50000
    venta = 51000
    scrapper.print_bitcoin_price(compra, venta)
    captured = capsys.readouterr()
    assert "Gracias por utilizar este scrapper." in captured.out
    assert "Los valores actuales del bitcoin son:" in captured.out
