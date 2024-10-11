import unittest
from unittest.mock import patch, MagicMock
from src.main import main  # Замените `your_module` на имя вашего модуля.

class MainTestCase(unittest.TestCase):

    @patch('builtins.input', side_effect=["1", "EXECUTED", "да", "в порядке возрастания", "да", "фраза", "нет"])
    @patch('your_module.get_transactions', return_value=[
        {"date": "2021-09-01T12:00:00Z", "description": "Транзакция 1", "from": "Счет 1",
         "to": "Счет 2", "operationAmount": {"amount": 1000, "currency": {"code": "RUB"}}}
    ])
    def test_main_json_input(self, mock_get_transactions):
        with patch('builtins.print') as mock_print:
            main()
            # Проверка, что основные части функции были вызваны
            mock_get_transactions.assert_called_once()
            self.assertIn("Добро пожаловать в программу работы с банковскими транзакциями.", [call[0][0] for call in mock_print.call_args_list])
            self.assertIn("Операции отфильтрованы по статусу EXECUTED", [call[0][0] for call in mock_print.call_args_list])
            self.assertIn("Распечатываю итоговый список транзакций...", [call[0][0] for call in mock_print.call_args_list])
            self.assertIn("Всего банковских операций в выборке: 1", [call[0][0] for call in mock_print.call_args_list])

    @patch('builtins.input', side_effect=["2", "CANCELED", "нет"])
    @patch('your_module.read_file_csv', return_value=[{"date": "2021-09-01T12:00:00Z", "description": "Транзакция 2",
                                                         "from": "Счет 3", "to": "Счет 4",
                                                         "operationAmount": {"amount": 2000, "currency": {"code": "USD"}}}])
    def test_main_csv_input(self, mock_read_file_csv):
        with patch('builtins.print') as mock_print:
            main()
            # Проверка, что функции были вызваны
            mock_read_file_csv.assert_called_once()
            self.assertIn("Для обработки выбран CSV-файл.", [call[0][0] for call in mock_print.call_args_list])

    @patch('builtins.input', side_effect=["3", "PENDING", "нет"])
    @patch('your_module.read_excel', return_value=[{"date": "2021-09-01T12:00:00Z", "description": "Транзакция 3",
                                                      "from": "Счет 5", "to": "Счет 6",
                                                      "operationAmount": {"amount": 3000, "currency": {"code": "EUR"}}}])
    def test_main_xlsx_input(self, mock_read_excel):
        with patch('builtins.print') as mock_print:
            main()
            # Проверка, что функции были вызваны
            mock_read_excel.assert_called_once()
            self.assertIn("Для обработки выбран XLSX-файл.", [call[0][0] for call in mock_print.call_args_list])

    @patch('builtins.input', side_effect=["4"])  # некорректный ввод
    @patch('builtins.print')
    def test_main_invalid_menu_option(self, mock_print):
        main()
        mock_print.assert_any_call("Введен некорректный номер.")

if __name__ == '__main__':
    unittest.main()
