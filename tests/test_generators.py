from src.generators import filter_by_currency
import pytest

try:
    def test_filter_by_currency(input_currency, exit_currency):
        filter_currency = filter_by_currency(input_currency, exit_currency)
        assert next(filter_currency)(input_currency) == exit_currency
except:
    StopIteration
    pass
