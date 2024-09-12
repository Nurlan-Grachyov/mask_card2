from typing import Any

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "acc_card, mask_acc_card",
    [
        ("1234564567898765", "1234 56** **** 8765"),
        ("счет 12345678900987654321", "счет **4321"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("", "Некорректный ввод"),
        ("Visa Platinum 70092289.063ю1", "Некорректный ввод"),
        ("счет 1230987654321", "Некорректный ввод"),
    ],
)
def test_mask_account_card(acc_card: str, mask_acc_card: str) -> Any:
    assert mask_account_card(acc_card) == mask_acc_card


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2.24-03-1/T02:26:18.671407") == "Некорректная дата"
    assert get_date("2024-03-11T02:") == "Некорректная дата"
    assert get_date("") == "Некорректная дата"
