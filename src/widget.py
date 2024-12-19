import re
from datetime import datetime

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(user_data: str) -> str:
    """Функция, которая принимает номер карты или счета и возвращает его замаскированным"""
    split_data = user_data.split(" ")
    filtered_user_data = ""
    for item in split_data:
        if item.isdigit():
            filtered_user_data = item
    if len(filtered_user_data) == 16:
        return get_mask_card_number(filtered_user_data)
    elif len(filtered_user_data) == 20:
        return get_mask_account(filtered_user_data)
    else:
        raise ValueError("Uncorrected data!")


def get_date(cur_date: str) -> str:
    """Функция, которая принимает дату в формате "2024-03-11T02:26:18.671407" возвращает строку в формате ДД.ММ.ГГГГ"""
    filtered_date = datetime.strptime(cur_date[:10], "%Y-%m-%d")
    return filtered_date.strftime("%d.%m.%Y")
