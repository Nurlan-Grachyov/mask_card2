bank_account = input().lower()


def mask_account_card(card_or_account: str) -> str:
    if "Счет" in card_or_account:
        """Шифрует номер счета"""
        slice_acc = card_or_account[5:21]
        mask_acc = card_or_account.replace(slice_acc, "**")
        return mask_acc
    else:
        """Шифрует номер карты"""
        slice_card = card_or_account[-10:-4]
        mask_card = card_or_account.replace(slice_card, "******")
        new_mask_card = mask_card[:-12] + " " + mask_card[-12:-8] + " " + mask_card[-8:-4] + " " + mask_card[-4:]
        return new_mask_card


print(mask_account_card(bank_account))