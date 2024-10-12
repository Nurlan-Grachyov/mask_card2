from collections import Counter

from src.search import count_categories, list_categories, search_description, transactions


def test_search_description():
    assert search_description(transactions, "Открытие вклада") == [
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        }
    ]


def test_count_categories():
    assert count_categories(transactions, list_categories) == Counter(
        {"Перевод организации": 2, "Перевод с карты на карту": 1}
    )
