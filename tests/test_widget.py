import pytest

from src.widget import get_date, mask_account_card


# mask_account_card
@pytest.mark.parametrize(
    "user_data, expected",
    [("VISA card 1234567890123456", "VISA card 1234 56** **** 3456"), ("12345678901234567890", "**7890")],
)
def test_mask_account_card_choosing(user_data, expected):
    assert mask_account_card(user_data) == expected


@pytest.mark.parametrize(
    "user_data, expected",
    [
        ("VISA card 1234567890123456", "VISA card 1234 56** **** 3456"),
        ("12345678901234567890", "**7890"),
        ("my card number 7685985647568756", "my card number 7685 98** **** 8756"),
        ("acc 76857132456598609875", "acc **9875"),
    ],
)
def test_mask_account_card_basic(user_data, expected):
    assert mask_account_card(user_data) == expected


@pytest.mark.parametrize(
    "user_data",
    [
        "card number 783497234u0329874",
        "234325325",
        "1234 1234 1234 1234",
        "idk",
    ],
)
def test_mask_account_card_invalid_input(user_data):
    with pytest.raises(ValueError):
        mask_account_card(user_data)


# get_date
def test_get_date_input(fixture_date):
    for i in fixture_date:
        assert get_date(i)


def test_get_date_invalid_date(fixture_invalid_date):
    for i in fixture_invalid_date:
        with pytest.raises(ValueError):
            get_date(i)
