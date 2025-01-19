import codecs
import json
import os
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/utils.log', 'w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_list_of_operations(file_path: str) -> list:
    """Возвращает список словарей с данными о финансовых транзакциях"""
    if os.path.isfile(file_path) and os.path.getsize(file_path) != 0:
        with codecs.open(file_path, "r", "utf_8_sig") as json_file:
            operations = json.load(json_file)
        if isinstance(operations, list):
            return operations
    return []
