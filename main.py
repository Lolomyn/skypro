from src.widget import get_date, mask_account_card

CARD_NUMBER_STANDARD_LENGTH = 16
ACCOUNT_NUMBER_STANDARD_LENGTH = 20


def get_info():
    # print(mask_account_card(input()))
    # print(mask_account_card(input()))
    print(get_date(input()))


if __name__ == "__main__":
    get_info()
