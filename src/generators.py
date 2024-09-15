import random

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "", "code": "USD"}},
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
except:
    StopIteration
    pass


try:

    def transaction_descriptions(data):
        for y in data:
            yield y["description"]

    descriptions = transaction_descriptions(transactions)
    for a in range(5):
        print(next(descriptions))
except:
    StopIteration
pass

result = ""
try:

    def card_number_generator(card):
        while True:
            card += str(random.randint(1, 9))
            if len(card) == 16:
                true_card = card[:4] + " " + card[4:8] + " " + card[8:12] + "  " + card[12:16]
                yield true_card

    gen = card_number_generator(result)
    print(next(gen))
except:
    StopIteration
pass
