import random

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]

try:

    def filter_by_currency(data, currency):
        if len(data) > 1:
            for x in data:
                if x.get("operationAmount").get("currency").get("name") == currency:
                    yield x


    usd_transactions = filter_by_currency(transactions, "USD")
    for i in range(2):
        print(next(usd_transactions))
except StopIteration:
    pass


try:

    def transaction_descriptions(data):
        for y in data:
            yield y["description"]

    descriptions = transaction_descriptions(transactions)
    for a in range(5):
        print(next(descriptions))
except StopIteration:
    pass


try:
    def card_number_generator(start, stop):
        while True:
            card = '0000 0000 0000 000'
            card += str(start)
            if start > stop:
                exit()
            start += 1
            yield card


    for card_number in card_number_generator(1, 5):
        print(card_number)

except StopIteration:
    pass
