from unittest.mock import mock_open, patch

import pandas as pd

from src.csv_xlsx import get_data_from_csv, get_data_from_excel


def test_get_data_from_csv():
    mock_data = "id;state;date;amount;currency_name;currency_code;from;to;description\n1;2;3;4;5;6;7;8;9\n"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        res = get_data_from_csv("fake")
        assert res == [
            {
                "id": "1",
                "state": "2",
                "date": "3",
                "amount": "4",
                "currency_name": "5",
                "currency_code": "6",
                "from": "7",
                "to": "8",
                "description": "9",
            }
        ]


@patch('pandas.read_excel')
def test_get_data_from_excel(mock_read_excel):
    mock_data = pd.DataFrame({"id": ["1", "2", "3"], "Name": ["Sarah", "Mark", "John"]})
    mock_read_excel.return_value = mock_data
    result = get_data_from_excel("fake")
    expected = [
        {"id": "1", "Name": "Sarah"},
        {"id": "2", "Name": "Mark"},
        {"id": "3", "Name": "John"},
    ]
    assert result == expected
