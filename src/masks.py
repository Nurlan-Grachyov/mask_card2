def get_mask_card_number(card: str) -> str:
    """Возвращает реквизиты карты с зашифрованным номером"""
    slice_card = card[-10:-4]
    mask_card = card.replace(slice_card, "******")
    new_mask_card = mask_card[:-12] + " " + mask_card[-12:-8] + " " + mask_card[-8:-4] + " " + mask_card[-4:]
    return new_mask_card


def get_mask_account(acc: str) -> str:
    """Возвращает реквизиты счета с зашифрованным номером"""
    slice_acc = acc[-20:-4]
    mask_acc = acc.replace(slice_acc, "**")
    return mask_acc
