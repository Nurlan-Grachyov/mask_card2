import os

import requests
from dotenv import load_dotenv


def conversion_currency(transaction) -> float:
    """Функция, конвертирующая сумму из иностранной валюты в рубли"""
    from_curr = transaction["operationAmount"]["currency"]["code"]
    amount = float(transaction["operationAmount"]["amount"])

    load_dotenv()
    access_key = os.getenv("access_key")

    headers = {"apikey": access_key}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_curr}&amount={amount}"

    if from_curr == "RUB":
        return amount
    elif from_curr != "RUB":
        result = requests.get(url, headers=headers)
        new_amount = result.json()
        return new_amount["operationAmount"]["amount"]


if __name__ == "__main__":
    print(
        conversion_currency(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
    )
