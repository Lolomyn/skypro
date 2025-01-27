import codecs
import json
import logging
import os
from collections import Counter, defaultdict

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_list_of_operations(file_path: str) -> list:
    """Возвращает список словарей с данными о финансовых транзакциях"""
    logger.info(f"Ищутся транзакции по адресу: {file_path}")
    if os.path.isfile(file_path) and os.path.getsize(file_path) != 0:
        logger.info(f"Файл [{file_path}] существует. Открывается для чтения...")
        with codecs.open(file_path, "r", "utf_8_sig") as json_file:
            logger.info("Загрузка данных из json файла...")
            operations = json.load(json_file)
        if isinstance(operations, list):
            logger.info("Данные валидны, возвращается список транзакций")
            return operations
    logger.error("Данные некорректны, возвращается пустой список")
    return []


def get_dict_of_categories_and_operations(list_of_transactions: list, list_of_categories: list) -> dict:
    """Возвращает словарь вида: {Название категории: количество операций данной категории}"""
    # инициализация пустого словаря с ключами - категориями
    result_dict = {}
    for category in list_of_categories:
        result_dict[category] = 0

    # список, в котором находится транзакции только по переданным категориям
    result_list = [
        i["description"]
        for i in list_of_transactions
        if i.get("description") is not None and i["description"] in list_of_categories
    ]

    # подсчет операций по категориям
    counter = Counter(result_list)

    # если категория передана, но операций нет, добавление ее в итоговый словарь
    for key, value in result_dict.items():
        if key not in counter:
            counter[key] = value
    result_dict = counter

    return result_dict
