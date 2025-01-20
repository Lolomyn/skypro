from unittest.mock import patch

import pytest

from src.external_api import convert_rate_to_rub, get_amount


def test_get_amount_valid_and_not_converted(fixture_get_amount_valid):
    assert get_amount(fixture_get_amount_valid) == 31957.58


def test_get_amount_valid_and_converted(fixture_get_amount_to_convert):
    def mock_func(a, b):
        return 123

    with patch("src.external_api.convert_rate_to_rub", new=mock_func):
        result = get_amount(fixture_get_amount_to_convert)
        assert result == 123


def test_get_amount_empty_dict(fixture_get_amount_empty):
    with pytest.raises(ValueError):
        assert get_amount(fixture_get_amount_empty)


def test_get_amount_invalid_data(fixture_get_amount_invalid):
    with pytest.raises(ValueError):
        assert get_amount(fixture_get_amount_invalid)


def test_convert_rate_to_rub():
    with patch("json.loads", return_value={"success": True, "result": 1234}):
        result = convert_rate_to_rub("USD", 15)
        assert result == 1234
