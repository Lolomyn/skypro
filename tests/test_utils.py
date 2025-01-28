import json
from unittest.mock import mock_open, patch

from src.utils import get_list_of_operations, get_dict_of_categories_and_operations


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


def test_get_dict_of_categories_and_operations():
    categories = ['1', '2', '3']
    output_list = [
        {"description": "1", "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"},
        {"description": "2", "from": "MasterCard 7158300734726758"}
    ]

    expected = {'1': 1, '2': 1, '3': 0}
    assert get_dict_of_categories_and_operations(output_list, categories) == expected
