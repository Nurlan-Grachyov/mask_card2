import json
from unittest.mock import patch


from src.utils import get_transactions, get_sum


@patch("builtins.open")
def test_read_file(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert get_transactions("C:/Users/Nurlan/IT/Проекты/mask_card2/data/operations.json") == [{"test": "test"}]
    mock_file.read.return_value = json.dumps('{"DEBUG": true, "directory": "C:/Games/MudRunner/Media}')
    assert get_transactions("C:/Users/Nurlan/IT/Проекты/mask_card2/data/operations.json") == []
    mock_file.read.return_value = json.dumps([])
    assert get_transactions("C:/Users/Nurlan/IT/Проекты/mask_card2/data/operations.json") == []


@patch('requests.get')
def test_get_sum(mock_get):
    mock_get.return_value.json.return_value = {'success': True, 'terms': 'https://currencylayer.com/terms', 'privacy': 'https://currencylayer.com/privacy', 'query': {'from': 'USD', 'to': 'RUB', 'amount': 200000}, 'info': {'timestamp': 1727545324, 'quote': 94.224321}, 'result': 18844864.2}
    assert get_sum() == 963716013.16
