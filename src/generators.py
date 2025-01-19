from typing import Generator


def filter_by_currency(transactions: list, currency: str = "USD") -> Generator:
    """Создается итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction


# генератор описаний транзакций
def transaction_descriptions(transactions: list) -> Generator:
    """Генератор, который возвращает описания транзакций"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int = 1, end: int = 9999999999999999) -> Generator:
    """Генератор номеров банковских карт в формате ХХХХ ХХХХ ХХХХ ХХХХ, где Х - цифра номера карты

    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999
    """
    if start < 1 or start > 9999999999999999 or end > 9999999999999999 or end < 1 or start > end:
        raise ValueError("Uncorrected data! Check ur input, pls")
    else:
        for i in range(start, end + 1):
            card_number = f"{i: 016d}"
            card_number_with_spaces = " ".join([card_number[i: i + 4] for i in range(0, len(f"{i:016d}"), 4)])
            yield card_number_with_spaces
