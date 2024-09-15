def get_mask_card_number(card: str) -> str:
    """Возвращает реквизиты карты с зашифрованным номером"""
    counter = 0
    for num in card:
        if num.isdigit():
            counter += 1
    if counter == 16 and card[-16:].isdigit():
        slice_card = card[-10:-4]
        mask_card = card.replace(slice_card, "******")
        new_mask_card = mask_card[:-12] + " " + mask_card[-12:-8] + " " + mask_card[-8:-4] + " " + mask_card[-4:]
        return new_mask_card
    else:
        return "Некорректный ввод"


def get_mask_account(acc: str) -> str:
    """Возвращает реквизиты счета с зашифрованным номером"""
    counter = 0
    for num in acc:
        if num.isdigit():
            counter += 1
    if counter == 20 and acc[-20:].isdigit():
        slice_acc = acc[-20:-4]
        mask_acc = acc.replace(slice_acc, "**")
        return mask_acc
    else:
        return "Некорректный ввод"


if __name__ == "__main__":
    print(get_mask_card_number("123456789098765"))

    print(get_mask_account("1234567890098754321"))
