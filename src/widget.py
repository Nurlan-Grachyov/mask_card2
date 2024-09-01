from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_account: str) -> str:
    """Возвращает реквизиты счета или карты с зашифрованным номером"""
    if bank_account.lower().startswith("счет"):
        return get_mask_account(bank_account)
    else:
        return get_mask_card_number(bank_account)


def get_date(date: str) -> str:
    """Преобразует дату из формата гггг-мм-ддТч:м:с.мс в дд.мм.гггг"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


if __name__ == "__main__":
    # Ввод счета или номера карты
    bank_account = str(input().lower())
    print(mask_account_card(bank_account))

    # Ввод даты
    data = str(input())
    print(get_date(data))
