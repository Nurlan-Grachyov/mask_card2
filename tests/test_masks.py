import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card, new_card",
    [
        ("", "Некорректный ввод"),
        ("", "Некорректный ввод"),
        ("1234567890098765", "1234 56** **** 8765"),
        ("qwertyuiop[];lk", "Некорректный ввод"),
    ],
)
def test_get_mask_card_number(card, new_card):
    assert get_mask_card_number(card) == new_card


def test_get_mask_account():
    assert get_mask_account("12345678900987653456") == "**3456"
    assert get_mask_account("1234567890098") == "Некорректный ввод"
    assert get_mask_account("") == "Некорректный ввод"
    assert get_mask_account("gfhgjhkfyu") == "Некорректный ввод"
