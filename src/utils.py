import json
from typing import Any

from src.external_api import conversion_currency


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
    data = get_transactions("C:/Users/Nurlan/IT/Проекты/mask_card2/data/operations.json")
    lst_str = []
    amount = []
    for i in data:
        if len(i) == 0:
            continue
        elif i["operationAmount"]["currency"]["code"] != "RUB":
            conv_curr = conversion_currency(
                "RUB", i["operationAmount"]["currency"]["code"], i["operationAmount"]["amount"]
            )
            amount.append(conv_curr)
        else:
            lst_str.append(i["operationAmount"]["amount"])
    for i in lst_str:
        amount.append(float(i))
    total_amount = sum(amount)
    return total_amount


if __name__ == "__main__":
    print(get_transactions("C:/Users/Nurlan/IT/Проекты/mask_card2/data/operations.json"))
    print(get_sum())
