import pytest

@pytest.fixture()
def get_mask_account(acc: str) -> str:
    """Возвращает реквизиты счета с зашифрованным номером"""
    if len(acc) == 20 and acc.isdigit():
        slice_acc = acc[-20:-4]
        mask_acc = acc.replace(slice_acc, "**")
    else:
        return 'Некорректный ввод'
    return mask_acc