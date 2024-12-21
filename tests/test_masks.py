import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number("1234567890123") == "1234 56** *012 3"
    assert get_mask_card_number("12345678901234") == "1234 56** **12 34"
    assert get_mask_card_number("123456789012345") == "1234 56** ***2 345"
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert get_mask_card_number("12345678901234567") == "1234 56** **** *4567"
    assert get_mask_card_number("123456789012345678") == "1234 56** **** **5678"
    assert get_mask_card_number("1234567890123456789") == "1234 56** **** ***6789"


def test_get_mask_account(fixture_account_number):
    assert get_mask_account(fixture_account_number) == "**7890"
