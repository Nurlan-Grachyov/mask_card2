import json
import os
from pathlib import Path
from typing import Any

PATH_TO_PROJECT = Path(__file__).resolve().parent.parent
PATH_TO_FILE = PATH_TO_PROJECT / "data" / "operations.json"


def get_transactions(file: str) -> Any:
    """Функция, возвращающая данные из файла json"""
    with open(file, encoding="UTF-8") as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            return []
        if len(data) == 0 or type(data) is not list:
            return []
        return data


if __name__ == "__main__":
    print(get_transactions(os.path.abspath(PATH_TO_FILE)))
