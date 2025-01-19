import codecs
import json
import os


def get_list_of_operations(file_path: str) -> list:
    """Возвращает список словарей с данными о финансовых транзакциях"""
    if os.path.isfile(file_path) and os.path.getsize(file_path) != 0:
        with codecs.open(file_path, "r", "utf_8_sig") as json_file:
            operations = json.load(json_file)
        if isinstance(operations, list):
            return operations
    return []
