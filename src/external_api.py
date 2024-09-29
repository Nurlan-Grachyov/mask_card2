import os
from typing import Any

import requests
from dotenv import load_dotenv


def conversion_currency(to_curr: str, from_curr: str, amount: str) -> Any:
    """Функция, конвертирующая сумму из иностранной валюты в рубли"""
    load_dotenv()
    access_key = os.getenv("access_key")
    url =  'https://api.tinkoff.ru/v1/currency_rates?from=USD&to=RUB'


    headers = {"accept": "application/json"}

    response = requests.get(url)

    result = response.json()
    return result['result']


if __name__ == "__main__":
    print(conversion_currency("RUB", "USD", "200000"))
