import json
import os
from pathlib import Path
from typing import Any

from src.external_api import conversion_currency

PATH_TO_PROJECT = Path(__file__).resolve().parent.parent
PATH_TO_FILE = PATH_TO_PROJECT / "data" / "operations.json"


def get_transactions(file: str) -> Any:
    """Функция, возвращающая данные из файла json"""
    with open(file, encoding="UTF-8") as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            return []
        if len(data) == 0 or type(data) is not list:
            return []
        return data


def get_sum() -> Any:
    """Функция, суммирующая суммы транзакций в рублях"""
    data = get_transactions(os.path.abspath(PATH_TO_FILE))
    lst_str = []
    amount = []
    for i in data:
        if len(i) == 0:
            continue
        elif i["operationAmount"]["currency"]["code"] == "RUB":
            lst_str.append(i["operationAmount"]["amount"])
        elif i["operationAmount"]["currency"]["code"] != "RUB":
            conv_curr = conversion_currency(
                "RUB", i["operationAmount"]["currency"]["code"], i["operationAmount"]["amount"]
            )
            amount.append(conv_curr)

    for i in lst_str:
        amount.append(float(i))
    total_amount = sum(amount)
    return total_amount


if __name__ == "__main__":
    print(get_transactions(os.path.abspath(PATH_TO_FILE)))

