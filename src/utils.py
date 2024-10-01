import json
import logging
import os
from pathlib import Path
from typing import Any

PATH_TO_PROJECT = Path(__file__).resolve().parent.parent
PATH_TO_FILE = PATH_TO_PROJECT / "data" / "operations.json"

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
fileHandler = logging.FileHandler(PATH_TO_PROJECT / "logs" / "utils.log", encoding="UTF-8", mode="w")
fileFormatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
fileHandler.setFormatter(fileFormatter)
logger.addHandler(fileHandler)


logger_mistake = logging.getLogger("utils")
logger_mistake.setLevel(logging.ERROR)
fileHandler_mistake = logging.FileHandler(PATH_TO_PROJECT / "logs" / "utils.log", encoding="UTF-8", mode="w")
fileFormatter_mistake = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
fileHandler_mistake.setFormatter(fileFormatter_mistake)
logger_mistake.addHandler(fileHandler_mistake)


def get_transactions(file: str) -> Any:
    """Функция, возвращающая данные из файла json"""
    with open(file, encoding="UTF-8") as f:
        try:
            logger.info("Получаем данные json файла")
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            logger_mistake.error("Ошибка! Некорректные данные json файла")
            return []
        if len(data) == 0 or type(data) is not list:
            logger_mistake.error("Ошибка! Либо файла пустой, либо файл не содержит список")
            return []
        return data


if __name__ == "__main__":
    print(get_transactions(os.path.abspath(PATH_TO_FILE)))
