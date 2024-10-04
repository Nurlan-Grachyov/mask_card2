import pandas as pd

from src.utils import PATH_TO_PROJECT

PATH_TO_EXCEL = PATH_TO_PROJECT / "files" / "file_Excel.xlsx"

reader = pd.read_csv(PATH_TO_EXCEL)
list_reader = reader.to_dict()
print(list_reader)
