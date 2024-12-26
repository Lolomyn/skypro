import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


# filter_by_currency
def test_filter_by_currency(fixture_transaction):
    expected_result = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 5,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
    ]
    result = list(filter_by_currency(fixture_transaction))

    assert result == expected_result


def test_filter_by_currency_no_currency(fixture_transaction):
    with pytest.raises(StopIteration):
        result = filter_by_currency(fixture_transaction, "YEN")
        assert next(result)


def test_filter_by_currency_invalid_input(fixture_transaction_invalid):
    with pytest.raises(KeyError):
        result = filter_by_currency(fixture_transaction_invalid)
        assert next(result)


# transaction_descriptions
def test_transaction_descriptions(fixture_transaction):
    expected_result = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод организации",
        "Перевод со счета на счет",
    ]
    result = list(transaction_descriptions(fixture_transaction))

    assert result == expected_result


def test_transaction_descriptions_invalid_input(fixture_transaction_invalid):
    with pytest.raises(KeyError):
        result = transaction_descriptions(fixture_transaction_invalid)
        assert next(result)


def test_transaction_descriptions_end_iteration(fixture_transaction):
    with pytest.raises(StopIteration):
        result = transaction_descriptions(fixture_transaction)
        for _ in range(1, 8):
            assert next(result)


# card_number_generator
def test_card_number_generator():
    expected_result = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    result = list(card_number_generator(1, 5))
    assert result == expected_result


@pytest.mark.parametrize(
    "data", [(-1, -1), (-1, 123), (123, -1), (1, 10000000000000000), (10000000000000000, 1), (12, 8)]
)
def test_card_number_generator_invalid_args(data):
    with pytest.raises(ValueError):
        result = list(card_number_generator(data[0], data[1]))
        assert result
