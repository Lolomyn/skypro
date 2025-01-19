import logging


logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/masks.log', 'w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает номер карты и возвращает маску номера по правилу XXXX XX** **** XXXX

    Примеры масок карты:
        13 - 1234 56** *012 3
        14 - 1234 56** **12 34
        15 - 1234 56** ***2 345
        16 - 1234 56** **** 3456
        17 - 1234 56** **** *4567
        18 - 1234 56** **** **5678
        19 - 1234 56** **** ***6789
    """

    star = "*"
    # высчитываемые части маски
    first_part_mask = f"{str(card_number)[0:4]} {str(card_number)[4:6]}**"
    second_part_mask = abs(len(card_number) - 16)

    if len(card_number) < 16:
        return (
            f"{first_part_mask} {star * (4 - second_part_mask)}{card_number[-4:second_part_mask - 4]} "
            f"{card_number[-(4 - second_part_mask):]}"
        )
    return f"{first_part_mask} {star * 4} {star * second_part_mask}{card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает номер счета и возвращает маску номера по правилу **XXXX"""
    return f"**{account_number[-4:]}"
