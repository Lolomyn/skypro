from .masks import get_mask_account, get_mask_card_number


def mask_account_card(user_data: str) -> str:
    """Функция, которая принимает номер карты или счета и возвращает его замаскированным"""
    return (
        get_mask_account(user_data.split()[-1])
        if len(user_data.split()[-1]) == 20
        else get_mask_card_number(user_data.split()[-1])
    )


def get_date(cur_date: str) -> str:
    """Функция, которая принимает дату в формате "2024-03-11T02:26:18.671407" возвращает строку в формате ДД.ММ.ГГГГ"""
    return f"{cur_date[:10].split('-')[2]}.{cur_date[:10].split('-')[1]}.{cur_date[:10].split('-')[0]}"

