from src.utils import get_transactions


def trans():
    conv = {'success': True, 'terms': 'https://currencylayer.com/terms', 'privacy': 'https://currencylayer.com/privacy', 'query': {'from': 'USD', 'to': 'RUB', 'amount': 200000}, 'info': {'timestamp': 1727545324, 'quote': 94.224321}, 'result': 18844864.2}
    return conv


def get_sum():
    """Функция, суммирующая суммы транзакций в рублях"""
    data = get_transactions("C:/Users/Nurlan/IT/Проекты/mask_card2/data/operations.json")
    lst_str = []
    amount = []
    for i in data:
        if len(i) == 0:
            continue
        elif i["operationAmount"]["currency"]["code"] != "RUB":
            conv_curr = trans()
            amount.append(conv_curr['result'])
        else:
            lst_str.append(i["operationAmount"]["amount"])
    for i in lst_str:
        amount.append(float(i))
    total_amount = sum(amount)
    return total_amount

print(get_sum())
