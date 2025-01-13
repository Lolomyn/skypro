import json
import os

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_amount(transaction_info: dict) -> float:
    """Возвращает сумму транзакции в рублях
    Операции в USD или EUR предварительно конвертируются в рубли по текущему курсу"""
    currency: str = transaction_info["operationAmount"]["currency"]["code"]
    amount: float = transaction_info["operationAmount"]["amount"]

    if currency == "RUB":
        return amount
    else:
        return convert_rate_to_rub(currency, amount)


def convert_rate_to_rub(currency: str, amount: float) -> float:
    """Функция для конвертации переданной валюты в RUB"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    payload: dict = {}
    headers = {"apikey": API_KEY}

    response = requests.request("GET", url, headers=headers, data=payload)

    result = response.text

    exchange_amount: dict = json.loads(result)
    exchange_amount_value: float = exchange_amount["result"]

    return exchange_amount_value


print(get_amount({
		"id": 441945886,
		"state": "EXECUTED",
		"date": "2019-08-26T10:50:58.294041",
		"operationAmount": {
			"amount": "31957.58",
			"currency": {
				"name": "руб.",
				"code": "USD"
			}
		},
		"description": "Перевод организации",
		"from": "Maestro 1596837868705199",
		"to": "Счет 64686473678894779589"
	}))
