from src.masks import get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


my_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "20-07-03"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14"},
]


def get_info():
    pass
    # print(mask_account_card(input()))
    # print(mask_account_card(input()))
    # print(get_date(input()))
    print(filter_by_state(my_list, ""))
    # print(sort_by_date(my_list))
    # print(get_mask_card_number("1234567890123"))


if __name__ == "__main__":
    get_info()
