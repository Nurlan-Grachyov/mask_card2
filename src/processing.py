from typing import Any

def filter_by_state(start_list: list[dict[str, object]], state: str = "EXECUTED") -> list[dict[str, object]]:
    """Сортировка списка словарей по ключу state"""
    list = []
    for i in start_list:
        if i["state"] == state:
            list.append(i)
    return list


def sort_by_date(list_d: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Сортировка списка словарей по дате в порядке убывания"""
    sorted_list = sorted(list_d, key=lambda x: x["date"], reverse=reverse)
    return sorted_list


if __name__ == "__main__":
    lst = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(filter_by_state(lst))

    list_date = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(sort_by_date(list_date))
