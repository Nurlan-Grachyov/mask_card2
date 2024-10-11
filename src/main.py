import os

from _datetime import datetime

from src.files import PATH_TO_CSV, PATH_TO_EXCEL, read_excel, read_file_csv
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.utils import PATH_TO_FILE, get_transactions


def main():
    """Отвечает за основную логику проекта с пользователем и связывает функциональности между собой."""
    global filter, filter_transaction_date
    print("Добро пожаловать в программу работы с банковскими транзакциями.")
    print(
        """Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
    )

    user_input_file = input("Введите номер пункта: ")
    if user_input_file == "1":
        print("Для обработки выбран JSON-файл.")
        transactions_from_file = get_transactions(os.path.abspath(PATH_TO_FILE))
    elif user_input_file == "2":
        print("Для обработки выбран CSV-файл.")
        transactions_from_file = read_file_csv(PATH_TO_CSV)
    elif user_input_file == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions_from_file = read_excel(PATH_TO_EXCEL)
    else:
        print("Введен некорректный номер.")
        return


    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
        user_input_state = input("Введите статус для фильтрации: ").upper()
        if user_input_state != "EXECUTED" and user_input_state != "CANCELED" and user_input_state != "PENDING":
            print(f"Статус операции {user_input_state} недоступен.")
            continue
        print(f"Операции отфильтрованы по статусу {user_input_state}")
        filter = filter_by_state(transactions_from_file, user_input_state)
        break


    print("Отсортировать операции по дате? Да/Нет")
    user_input_date = input("Введите да или нет ").lower()
    if user_input_date == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        user_input_up_down = input("в порядке убывания / в порядке возрастания ").lower()
        if user_input_up_down == "в порядке убывания" or user_input_up_down == "в порядке возрастания":
            filter_transaction_date = sort_by_date(filter, user_input_up_down)
        else:
            print("Введен некорректный ответ.")
            return
    elif user_input_date == "нет":
        filter_transaction_date = filter
    else:
        print("Введен некорректный ответ.")
        return


    print("Выводить только рублевые транзакции? Да/Нет")
    user_input_curr = input("Введите да или нет: ").lower()
    if user_input_curr == "да":
        rub_trans = []
        for trans in filter_transaction_date:
            if trans["operationAmount"]["currency"]["code"] == "RUB":
                rub_trans.append(trans)
    elif user_input_curr == "нет":
        rub_trans = []
        for trans in filter_transaction_date:
            rub_trans.append(trans)
    else:
        print("Введен некорректный ответ.")
        return


    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    sort_by_word = input("Введите да или нет: ").lower()
    if sort_by_word == "да":
        sort_by_word_yes = input("Введите слово для фильтрации: ")
        trans_word = []
        for trans in rub_trans:
            if sort_by_word_yes in trans["description"]:
                trans_word.append(trans)
    elif sort_by_word == "нет":
        trans_word = []
        for trans in rub_trans:
            trans_word.append(trans)
    else:
        print("Введен некорректный ответ.")
        return
    if len(trans_word) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return


    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(trans_word)}\n")


    for trans in trans_word:
        if trans.get("from") and trans.get("to"):
            date = trans.get("date", "")
            bad_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
            correct_date = bad_date.strftime("%d.%m.%Y")
            description = trans.get("description", "")
            masked_card_from = get_mask_card_number(str(trans.get("from")))
            masked_card_to = get_mask_card_number(str(trans.get("to")))
            masked_acc_from = get_mask_account(str(trans.get("from")))
            masked_acc_to = get_mask_account(str(trans.get("to")))
            amount = trans["operationAmount"]["amount"]
            if "Счет" in (trans.get("from", "") or "") and "Счет" in (trans.get("to", "") or ""):
                print(f"{correct_date} {description}")
                print(f"Счет: {masked_acc_from} -> Счет: {masked_acc_to}")
                if trans.get("code") == "RUB":
                    print(f"Сумма: {amount} руб.\n")
                else:
                    print(f'Сумма: {amount} {trans["operationAmount"]["currency"]["code"]}\n')
            elif "Счет" in (trans.get("to", "") or ""):
                print(f"{correct_date} {description}")
                print(f"Счет: {masked_acc_to}")
                if trans.get("code") == "RUB":
                    print(f"Сумма: {amount} руб.\n")
                else:
                    print(f'Сумма: {amount} {trans["operationAmount"]["currency"]["code"]}\n')
            else:
                formatted_card_from = get_mask_card_number(masked_card_from)
                formatted_card_to = get_mask_card_number(masked_card_to)
                print(f"{correct_date} {description}")
                print(f"Транзакция: {formatted_card_from} -> {formatted_card_to}")
                if trans.get("code") == "RUB":
                    print(f"Сумма: {amount} руб.\n")
                else:
                    print(f'Сумма: {amount} {trans["operationAmount"]["currency"]["code"]}\n')


main()
