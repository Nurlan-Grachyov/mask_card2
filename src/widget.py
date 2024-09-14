from typing import Any

from dateutil import parser

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_acc: str) -> str:
    """Возвращает реквизиты счета или карты с зашифрованным номером"""
    counter = 0
    for num in bank_acc:
        if num.isdigit():
            counter += 1
    if counter == 20:
        return get_mask_account(bank_acc)
    elif counter == 16:
        return get_mask_card_number(bank_acc)
    else:
        return "Некорректный ввод"


def get_date(date: str) -> Any:
    """Преобразует дату из формата гггг-мм-ддТч:м:с.мс в дд.мм.гггг"""
    bad_result = "Некорректная дата"
    if date:
        try:
            parsed = parser.parse(date).strftime("%d.%m.%Y")
            return parsed
        except parser.ParserError:
            pass
    return bad_result


if __name__ == "__main__":
    # Ввод счета или номера карты
    bank_account = str(input("Введите карту или счет ").lower())
    print(mask_account_card(bank_account))

    # Ввод даты
    data = str(input("Введите дату "))
    print(get_date(data))
