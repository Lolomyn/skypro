import re


def filter_by_state(list_of_dicts: list, state_key_value: str = "EXECUTED") -> list:
    """Функция, которая возвращает список словарей, значение ключа state которых соответствует указанному"""
    return [i for i in list_of_dicts if i["state"] == state_key_value]


def sort_by_date(list_of_dicts: list, sort_order: bool = True) -> list:
    """Функция, которая возвращает отсортированный список словарей по дате (в порядке убывания или возрастания)"""
    return sorted(list_of_dicts, key=lambda x: x["date"], reverse=sort_order)


def search_by_query(list_of_transactions: list, search_string: str) -> list:
    """ Поиск банковских операций, в описании которых будет фигурировать искомая информация"""
    search_string = search_string.lower()
    result_list = []
    for transaction in list_of_transactions:
        if transaction:
            if transaction.get('description') is not None:
                transaction['description'] = transaction['description'].lower()
                result = re.search(search_string, transaction['description'])
                if result:
                    result_list.append(transaction)

    return result_list
