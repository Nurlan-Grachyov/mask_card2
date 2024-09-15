from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
import pytest


def test_filter_by_currency(input_currency, exit_currency):
    filter_currency = filter_by_currency(input_currency, exit_currency)
    try:
        result = next(filter_currency)
        assert result["currency"]["name"] == exit_currency
    except StopIteration:
        pass


@pytest.mark.parametrize(
    "input_descriptions, exit_descriptions",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            "Перевод организации",
            "Перевод со счета на счет",
        ),
    ],
)
def test_transaction_descriptions(input_descriptions, exit_descriptions):

    descriptions = transaction_descriptions(input_descriptions, exit_descriptions)
    assert next(descriptions) == exit_descriptions


@pytest.mark.parametrize(
    "card, new_card",
    [
        ("0000 0000 0000 000", "0000 0000 0000 0001"),
        ("0000 0000 0000 000", "0000 0000 0000 0002"),
        ("0000 0000 0000 000", "0000 0000 0000 0003"),
        ("0000 0000 0000 000", "0000 0000 0000 0004"),
        ("0000 0000 0000 000", "0000 0000 0000 0005"),
    ],
)
def test_card_number_generator(card, new_card):
    number_generator = card_number_generator(card, new_card)
    assert next(number_generator) == new_card
