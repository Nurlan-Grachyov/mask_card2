from typing import Any

import pytest


@pytest.fixture()
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


@pytest.fixture()
def get_date(date: str) -> str:
    """Преобразует дату из формата гггг-мм-ддТч:м:с.мс в дд.мм.гггг"""
    if len(date) == 26 and date[8:10].isdigit() and date[5:7].isdigit() and date[:4].isdigit():
        return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    else:
        return "Некорректная дата"


@pytest.fixture()
def sort_by_date(list_d: list[dict[str, Any]], reverse: bool) -> list[dict[str, Any]]:
    """Сортировка списка словарей по дате в порядке убывания"""
    for i in list_d:
        if "date" in i:
            if reverse:
                sorted_list = sorted(list_d, key=lambda x: x["date"], reverse=True)
            elif not reverse:
                sorted_list = sorted(list_d, key=lambda x: x["date"], reverse=False)
            else:
                sorted_list = sorted(list_d, key=lambda x: x["date"], reverse=True)
        else:
            return "Даты нет"
        return sorted_list
