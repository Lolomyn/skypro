def filter_by_state(list_of_dicts: list, state_key_value: str = "EXECUTED") -> list:
    """Функция, которая возвращает список словарей, значение ключа state которых соответствует указанному"""
    return [i for i in list_of_dicts if i["state"] == state_key_value]


def sort_by_date(list_of_dicts: list, sort_order: bool = True) -> list:
    """Функция, которая возвращает отсортированный список словарей по дате (в порядке убывания или возрастания)"""
    return sorted(list_of_dicts, key=lambda x: x["date"], reverse=sort_order)
