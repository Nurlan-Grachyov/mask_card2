from unittest.mock import patch

from src.files import read_file_csv, read_excel


@patch("src.files.read_file_csv")
def test_read_csv(mock):
    mock.return_value = {
        "Name": {0: "Alice", 1: "Bob", 2: "Charlie"},
        "Age": {0: 25, 1: 30, 2: 35},
        "Gender": {0: "Female", 1: "Male", 2: "Male"},
    }
    assert read_file_csv("../files/file.csv") ==  {
        "Name": {0: "Alice", 1: "Bob", 2: "Charlie"},
        "Age": {0: 25, 1: 30, 2: 35},
        "Gender": {0: "Female", 1: "Male", 2: "Male"},
    }


@patch("src.files.read_excel")
def test_read_file_excel(mock_return):
    mock_return.return_value = {
        "League": {
            0: "English Premier League (1)",
            1: "Spain Primera Division (1)",
            2: "English Premier League (1)",
            3: "German 1. Bundesliga (1)",
            4: "Spain Primera Division (1)",
            5: "Italian Serie A (1)",
        },
        "Name": {
            0: "Manchester City",
            1: "Real Madrid",
            2: "Liverpool",
            3: "FC Bayern München",
            4: "FC Barcelona",
            5: "Juventus",
        },
        "TransferBudget": {0: 176000000, 1: 188500000, 2: 90000000, 3: 100000000, 4: 180500000, 5: 105000000},
        "Unnamed: 0": {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
    }

    assert read_excel("../files/file.xlsx") == {
        "League": {
            0: "English Premier League (1)",
            1: "Spain Primera Division (1)",
            2: "English Premier League (1)",
            3: "German 1. Bundesliga (1)",
            4: "Spain Primera Division (1)",
            5: "Italian Serie A (1)",
        },
        "Name": {
            0: "Manchester City",
            1: "Real Madrid",
            2: "Liverpool",
            3: "FC Bayern München",
            4: "FC Barcelona",
            5: "Juventus",
        },
        "TransferBudget": {0: 176000000, 1: 188500000, 2: 90000000, 3: 100000000, 4: 180500000, 5: 105000000},
        "Unnamed: 0": {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
    }
