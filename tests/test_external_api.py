from typing import Any
from unittest.mock import patch

from src.external_api import conversion_currency



@patch("requests.get")
def test_conversion_currency(mock_get: Any) -> Any:
    mock_get.return_value.json.return_value = 31957.58
    assert (
            conversion_currency(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        == 31957.58
)
