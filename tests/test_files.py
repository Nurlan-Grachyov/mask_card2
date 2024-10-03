from unittest.mock import patch
from src.files import read_file_csv
from src.utils import PATH_TO_PROJECT

PATH_TO_FILE = PATH_TO_PROJECT / "files" / "files.csv"


@patch('to_dict')
def test_read_csv(mock):
    mock.return_value = {
        "Name": {0: "Alice", 1: "Bob", 2: "Charlie"},
        "Age": {0: 25, 1: 30, 2: 35},
        "Gender": {0: "Female", 1: "Male", 2: "Male"},
    }
    assert read_file_csv(PATH_TO_FILE) == {
        "Name": {0: "Alice", 1: "Bob", 2: "Charlie"},
        "Age": {0: 25, 1: 30, 2: 35},
        "Gender": {0: "Female", 1: "Male", 2: "Male"},
    }
