import os

from src.files import read_file_csv, PATH_TO_CSV, read_excel, PATH_TO_EXCEL
from src.processing import filter_by_state
from src.utils import get_transactions, PATH_TO_FILE


def main():
    print("Добро пожаловать в программу работы с банковскими транзакциями.")
    print(
        """Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
    )


    def get_transactions_from_file():
        while True:
            user_input_file = input("Введите номер пункта: ")
            if user_input_file == "1":
                print("Для обработки выбран JSON-файл.")
                transactions_from_file = get_transactions(os.path.abspath(PATH_TO_FILE))
                return transactions_from_file
            elif user_input_file == "2":
                print("Для обработки выбран CSV-файл.")
                transactions_from_file = read_file_csv(PATH_TO_CSV)
                return transactions_from_file
            elif user_input_file == "3":
                print("Для обработки выбран XLSX-файл.")
                transactions_from_file = read_excel(PATH_TO_EXCEL)
                return transactions_from_file
            else:
                print("Введен некорректный номер. Попробуйте заново.")
                continue


    def filter_by_state_main(transactions):
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
            print(filter_by_state(transactions, user_input_state))
            break


    print(filter_by_state_main(get_transactions_from_file()))


#     while True:
#         print("Отсортировать операции по дате? Да/Нет")
#         user_input = input('Введите да или нет').lower()
#         if user_input == 'да':
#             print("Отсортировать по возрастанию или по убыванию?")
#             user_input = input().lower()
#             if user_input == 'по возрастанию':
#                 pass
#             elif user_input == 'по убыванию':
#                 pass
#             else:
#                 print(f"Введен некорректный ответ. Попробуйте заново.")
#                 continue
#         elif user_input == 'нет':
#             pass
#         else:
#             print(f"Введен некорректный ответ. Попробуйте заново.")
#             continue
#
#
#         while True:
#             print("Выводить только рублевые транзакции? Да/Нет")
#             user_input = input('Введите да или нет').lower()
#             if user_input == 'да':
#                 pass
#             elif user_input == 'нет':
#                 pass
#             else:
#                 print(f"Введен некорректный ответ. Попробуйте заново.")
#                 continue
#
#
#         while True:
#             print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
#             user_input = input('Введите да или нет').lower()
#             if user_input == 'да':
#                 user_input = input('Введите слово для фильтрации').lower()
#             elif user_input == 'нет':
#                 pass
#             else:
#                 print(f"Введен некорректный ответ. Попробуйте заново.")
#                 continue
#
#
#         print("Распечатываю итоговый список транзакций...")
#         print("Всего банковских операций в выборке: 4")

main()
