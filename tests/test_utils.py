import json
from unittest.mock import mock_open, patch

from src.utils import get_list_of_operations


def test_get_list_of_operations():
    mock_data = '[{"id": 1, "amount": 100}]'
    with patch("os.path.isfile", return_value=True):
        with patch("os.path.getsize", return_value=1):
            with patch("codecs.open", mock_open(read_data=mock_data)):
                with patch("json.load", return_value=json.loads(mock_data)):
                    result = get_list_of_operations("dummy_path.json")
                    assert result == json.loads(mock_data)


def test_get_list_of_operations_no_list():
    mock_data = '{"id": 1, "amount": 100}'
    with patch("os.path.isfile", return_value=True):
        with patch("os.path.getsize", return_value=1):
            with patch("codecs.open", mock_open(read_data=mock_data)):
                with patch("json.load", return_value=json.loads(mock_data)):
                    result = get_list_of_operations("dummy_path.json")
                    assert result == []


def test_get_list_of_operations_no_file():
    with patch("os.path.isfile", return_value=False):
        result = get_list_of_operations("dummy_path.json")
        assert result == []


def test_get_list_of_operations_empty_file():
    with patch("os.path.isfile", return_value=True):
        with patch("os.path.getsize", return_value=0):
            result = get_list_of_operations("dummy_path.json")
            assert result == []
