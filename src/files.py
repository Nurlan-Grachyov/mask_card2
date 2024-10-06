import logging

import pandas as pd

from src.utils import PATH_TO_PROJECT

PATH_TO_CSV = PATH_TO_PROJECT / "files" / "transactions.csv"
PATH_TO_EXCEL = PATH_TO_PROJECT / "files" / "transactions_excel.xlsx"

logger = logging.getLogger("files")
logger.setLevel(logging.INFO)
fileHandler = logging.FileHandler(PATH_TO_PROJECT / "logs" / "files.log", encoding="UTF-8", mode="w")
fileFormatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
fileHandler.setFormatter(fileFormatter)
logger.addHandler(fileHandler)


def read_file_csv(file):
    try:
        logger.info("Получаем данные файла")
        reader = pd.read_csv(file)
        list_reader = reader.to_dict()
        return list_reader
    except Exception:
        logger.error("Ошибка!")
        return []


def read_excel(file):
    try:
        logger.info("Получаем данные файла")

        data_excel = pd.read_excel(file)
        dict_data = data_excel.to_dict()
        return dict_data
    except Exception:
        logger.error("Ошибка!")

        return []


if __name__ == "__main__":
    print(read_file_csv(PATH_TO_CSV))
    print(read_excel(PATH_TO_EXCEL))
