from src.masks import get_mask_account, get_mask_card_number

"""Ввод пользователя"""
bank_account = str(input().lower())


def mask_account_card(bank_account: str) -> str:
    if bank_account.lower().startswith("счет"):
        """Шифрует номер счета"""
        # slice_acc = bank_account[5:21]
        # mask_acc = bank_account.replace(slice_acc, "**")
        # return mask_acc
        return get_mask_account(bank_account)
    else:
        """Шифрует номер карты"""
        # slice_card = card_or_account[-10:-4]
        # mask_card = card_or_account.replace(slice_card, "******")
        # new_mask_card = mask_card[:-12] + " " + mask_card[-12:-8] + " " + mask_card[-8:-4] + " " + mask_card[-4:]
        # return new_mask_card
        return get_mask_card_number(bank_account)


print(mask_account_card(bank_account))
data = str(input())


def get_date(date: str) -> str:
    """Определяем дату"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


print(get_date(data))
