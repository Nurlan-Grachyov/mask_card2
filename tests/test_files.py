from unittest.mock import Mock, patch

from src.files import read_excel, read_file_csv


@patch("src.files.pd.read_csv")  # Подменяем pd.read_csv
def test_read_file_csv_success(mock_read_csv):
    mock_read_csv.return_value = Mock(to_dict=Mock(return_value={"col1": [1, 2], "col2": [3, 5]}))
    result = read_file_csv("../files/file.csv")
    assert result == {"col1": [1, 2], "col2": [3, 5]}


@patch("src.files.pd.read_excel")
def test_read_file_excel(mock_return):
    mock_return.return_value = Mock(to_dict=Mock(return_value={"col1": [1, 2], "col2": [3, 4]}))
    result = read_excel("../files/file.xlsx")
    assert result == {"col1": [1, 2], "col2": [3, 4]}
