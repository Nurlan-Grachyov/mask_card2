import os
from typing import Any

import requests
from dotenv import load_dotenv


def conversion_currency(to_curr: str, from_curr: str, amount: str) -> Any:
    """Функция, конвертирующая сумму из иностранной валюты в рубли"""
    load_dotenv()
    access_key = os.getenv("access_key")
    url = (
        f"https://api.currencylayer.com/convert?from={from_curr}&to={to_curr}&amount={amount}&access_key={access_key}"
    )

    headers = {"access_key": "access_key=" + access_key}

    response = requests.get(url, headers=headers)

    result = response.json()
    return result


if __name__ == "__main__":
    print(conversion_currency("RUB", "USD", "200000"))
