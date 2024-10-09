import csv
import logging

import pandas as pd
from pandas import read_csv

from src.utils import PATH_TO_PROJECT

PATH_TO_CSV = PATH_TO_PROJECT / "files" / "transactions.csv"
PATH_TO_EXCEL = PATH_TO_PROJECT / "files" / "transactions_excel.xlsx"

logger = logging.getLogger("files")
logger.setLevel(logging.INFO)
fileHandler = logging.FileHandler(PATH_TO_PROJECT / "logs" / "files.log", encoding="UTF-8", mode="w")
fileFormatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
fileHandler.setFormatter(fileFormatter)
logger.addHandler(fileHandler)


def read_file_csv(file, state='EXECUTED'):
    # try:
        logger.info("Получаем данные файла")
        with open(file, encoding='UTF-8') as f:
            text = pd.read_csv(f)
            new_text = text.to_dict(orient='records')
            trans = text.loc[text.state == state]
            print(trans)
    # except Exception:
    #     logger.error("Ошибка!")
    #     return []
        return trans


def read_excel(file):
    try:
        logger.info("Получаем данные файла")
        data_excel = read_excel(file)
        return data_excel
    except Exception:
        logger.error("Ошибка!")
        return []


if __name__ == "__main__":
    print(read_file_csv(PATH_TO_CSV))
    # print(read_excel(PATH_TO_EXCEL))
