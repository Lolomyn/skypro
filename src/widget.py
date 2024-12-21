from datetime import datetime

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(user_data: str) -> str:
    """Функция, которая принимает номер карты или счета и возвращает его замаскированным.
    Номер карты или счета вводится без пробелов.

    Длина номера банковской карты может быть от 13 до 19 цифр.
    Самый распространённый вариант — 16 цифр.

    Номер счета всегда имеет 20 цифр.
    """

    split_data = user_data.split(" ")
    filtered_user_data = ""

    for item in split_data:
        if item.isdigit():
            filtered_user_data = item

    if 13 <= len(filtered_user_data) <= 19:
        return get_mask_card_number(filtered_user_data)
    elif len(filtered_user_data) == 20:
        return get_mask_account(filtered_user_data)
    else:
        raise ValueError(
            "Uncorrected data! " "The card number has 13 to 19 characters. " "The account number has 20 characters."
        )


def get_date(cur_date: str) -> str:
    """Функция, которая принимает дату в формате "2024-03-11T02:26:18.671407" возвращает строку в формате ДД.ММ.ГГГГ"""
    filtered_date = datetime.strptime(cur_date[:10], "%Y-%m-%d")
    return filtered_date.strftime("%d.%m.%Y")
