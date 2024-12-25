list_of_transactions = [
	{
		"id": 1,
		"state": "EXECUTED",
		"date": "2018-06-30T02:08:58.425572",
		"operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
		"description": "Перевод организации",
		"from": "Счет 75106830613657916952",
		"to": "Счет 11776614605963066702",
	},
	{
		"id": 2,
		"state": "EXECUTED",
		"date": "2019-04-04T23:20:05.206878",
		"operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
		"description": "Перевод со счета на счет",
		"from": "Счет 19708645243227258542",
		"to": "Счет 75651667383060284188",
	},
	{
		"id": 3,
		"state": "EXECUTED",
		"date": "2018-06-30T02:08:58.425572",
		"operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
		"description": "Перевод организации",
		"from": "Счет 75106830613657916952",
		"to": "Счет 11776614605963066702",
	},
	{
		"id": 4,
		"state": "EXECUTED",
		"date": "2019-04-04T23:20:05.206878",
		"operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
		"description": "Перевод со счета на счет",
		"from": "Счет 19708645243227258542",
		"to": "Счет 75651667383060284188",
	},
	{
		"id": 5,
		"state": "EXECUTED",
		"date": "2018-06-30T02:08:58.425572",
		"operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
		"description": "Перевод организации",
		"from": "Счет 75106830613657916952",
		"to": "Счет 11776614605963066702",
	},
	{
		"id": 6,
		"state": "EXECUTED",
		"date": "2019-04-04T23:20:05.206878",
		"operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
		"description": "Перевод со счета на счет",
		"from": "Счет 19708645243227258542",
		"to": "Счет 75651667383060284188",
	},
]


def filter_by_currency(transactions, currency="USD"):
	"""Создается итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
	for transaction in transactions:
		if transaction["operationAmount"]["currency"]["name"] == currency:
			yield transaction

x = filter_by_currency(list_of_transactions)
print(next(x))
print(next(x))


# генератор описаний транзакций
transaction_descriptions = (tr["description"] for tr in list_of_transactions)


def card_number_generator(start=1, end=9999999999999999) -> str:
	""" Генератор номеров банковских карт в формате ХХХХ ХХХХ ХХХХ ХХХХ, где Х - цифра номера карты

	Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999
	"""
	if start > end:
		raise ValueError("Стартовое значение не может быть больше конечного!")
	for i in range(start, end + 1):
		card_number = f"{i:016d}"
		card_number_with_spaces = ' '.join([card_number[i:i + 4] for i in range(0, len(card_number), 4)])
		yield card_number_with_spaces

