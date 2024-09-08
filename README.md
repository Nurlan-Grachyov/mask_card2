# Домашня работа 10.1

## Описание:
Продолжаем работу над виджетом банковских операций клиента. В этой домашней работе добавляются такие новые функции, как:
1. сортировка по состоянию, которое по умолчанию является EXECUTED;

````
def filter_by_state(start_list: list[dict[str, object]], state: str = "EXECUTED") -> list[dict[str, object]]:
    list = []
    for i in start_list:
        if i["state"] == state:
            list.append(i)
    return list
````

2. сортировка по дате. По умолчанию сортировка происходит в порядке убывания.

````
def sort_by_date(list_d: list[dict[str, str]], reverse: bool = True) -> list[dict[str, str]]:
    sorted_list = sorted(list_d, key=lambda x: x["date"], reverse=reverse)
    return sorted_list
````

## Инструкция
Перейти по ссылке PR из адресной строки.

## Примеры
1. Пример результата функции сортировки по состоянию:
````
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
````

2. Пример результата функции сортировки по дате:
````
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
````
