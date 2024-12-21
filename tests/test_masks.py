from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(fixture_card_number):
    for i in fixture_card_number:
        assert get_mask_card_number(i)


def test_get_mask_account(fixture_account_number):
    for i in fixture_account_number:
        assert get_mask_account(i)
