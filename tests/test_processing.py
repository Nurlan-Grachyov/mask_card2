from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "after_list, user_state, before_list",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        ([], "CANCELED", []),
        (
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [],
        ),
    ],
)
def test_filter_by_state(
    after_list: list[dict[str, object]], user_state: str, before_list: list[dict[str, object]]
) -> Any:
    assert filter_by_state(after_list, user_state) == before_list


def test_sort_by_date(input_1, reverse_1, exit_1, input_2, reverse_2, exit_2, input_3, reverse_3, exit_3) -> None:
    assert sort_by_date(input_1, reverse_1) == exit_1
    assert sort_by_date(input_2, reverse_2) == exit_2
    assert sort_by_date(input_3, reverse_3) == exit_3
