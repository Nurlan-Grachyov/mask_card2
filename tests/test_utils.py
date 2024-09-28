import json
from unittest.mock import patch

from src.utils import get_transactions, get_sum


@patch("builtins.open")
def test_read_file(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert get_transactions("C:/Users/Nurlan/IT/Проекты/mask_card2/data/operations.json") == [{"test": "test"}]
    mock_file.read.return_value = json.dumps('**')
    assert get_transactions("C:/Users/Nurlan/IT/Проекты/mask_card2/data/operations.json") == []
    mock_file.read.return_value = json.dumps([])
    assert get_transactions("C:/Users/Nurlan/IT/Проекты/mask_card2/data/operations.json") == []
    mock_file.read.return_value = json.dumps([])
    assert get_transactions("C:/Users/Nurlan/IT/Проекты/mask_card2/data/no_file.json") == []

@patch('requests.get')
def test_get_sum(mock_get):
    mock_get.return_value.json.return_value =
    assert get_sum() ==
