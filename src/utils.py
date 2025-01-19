import codecs
import json
import logging
import os

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
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
    logger.warning("Данные некорректны, возвращается пустой список")
    return []
