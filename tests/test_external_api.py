import os
from typing import Any
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import conversion_currency

load_dotenv()
access_key = os.getenv("access_key")
headers = {"access_key": "access_key=" + access_key}


@patch("requests.get")
def test_conversion_currency(mock_get: Any) -> Any:
    mock_get.return_value.json.return_value = {
        "success": True,
        "terms": "https://currencylayer.com/terms",
        "privacy": "https://currencylayer.com/privacy",
        "query": {"from": "USD", "to": "RUB", "amount": 200000},
        "info": {"timestamp": 1727518695, "quote": 94.224321},
        "result": 18844864.2,
    }
    assert conversion_currency("RUB", "USD", "200000") == 18844864.2
