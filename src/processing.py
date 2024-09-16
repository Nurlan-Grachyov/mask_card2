from typing import Any


def filter_by_state(start_list: list[dict[str, object]], state: str = "EXECUTED") -> list[dict[str, object]]:
    """Сортировка списка словарей по ключу state"""
    filtered_data = []
    for i in start_list:
        if i["state"] == state:
            filtered_data.append(i)
        else:
            continue
    return filtered_data


def sort_by_date(list_d: list[dict[str, Any]], reverse: str) -> Any:
    """Сортировка списка словарей по дате в порядке убывания"""
    sorted_list = []
    for i in list_d:
        if "date" in i:
            if reverse == "да":
                sorted_list = sorted(list_d, key=lambda x: x["date"], reverse=True)
            elif reverse == "нет":
                sorted_list = sorted(list_d, key=lambda x: x["date"])
            else:
                sorted_list = sorted(list_d, key=lambda x: x["date"], reverse=True)
        else:
            return "Даты нет"
    return sorted_list


if __name__ == "__main__":
    user_state = input("EXECUTED или CANCELED").upper()
    lst = [
        {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(filter_by_state(lst, user_state))

    user_reverse = input("да или нет")
    list_date = [
        {"id": 41428829, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(sort_by_date(list_date, user_reverse))
