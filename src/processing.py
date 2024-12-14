def filter_by_state(list_of_dict: list, state_key_value='EXECUTED') -> list:
	"""Функция, которая возвращает список словарей, значение ключа state которых соответствует указанному"""
	return [i for i in list_of_dict if i['state'] == state_key_value]

