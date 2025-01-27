import codecs
import logging
import json

from src.processing import search_by_query
from src.utils import get_list_of_operations, get_dict_of_categories_and_operations
from src.widget import mask_account_card

logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/main.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def main() -> None:
    """Место старта приложения"""
    # debug 1
    search_by_query(get_transactions("data/operations.json"), "Перевод")

    # debug 2
    operations = get_transactions("data/operations.json")
    get_dict_of_categories_and_operations(
        operations, ["Перевод со счета на счет", "Открытие вклада", "Оплата по QR-коду"]
    )

    # get_masked()
    # get_transactions()
    # logger.info("Работа программы завершена.")


def get_masked() -> None:
    """Запуск функция маскирования"""
    logger.info("Осуществляется ввод номера карты...")
    card_number = input("Введите номер карты без пробелов (16 символов): ")
    masked_card_number = mask_account_card(card_number)

    logger.info("Осуществляется ввод номера счета...")
    account_number = input("Введите номер счета без пробелов (20 символов): ")
    masked_account_number = mask_account_card(account_number)

    logger.info(
        f"Замаскированные данные: {masked_card_number}, {masked_account_number}. "
        f"Конец работы функции <get_masked>."
    )


def get_transactions(path) -> list:
    """Получает словарь с транзакциям из заданного .json файла"""
    logger.info(f"Получен список транзакций по пути: {path}")
    transactions = get_list_of_operations(path)
    logger.info(f"Получено транзакций: {len(transactions)}. Конец работы функции <get_transactions>")
    return transactions


if __name__ == "__main__":
    logger.info("Старт работы программы...")
    main()
