from src.csv_xlsx import get_data_from_csv, get_data_from_excel
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date, filtered_by_query
from src.utils import get_list_of_operations
from src.widget import get_date, mask_account_card


def get_user_output_format():
    data_choice = input(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n"""
    )

    while True:
        if data_choice == "1":
            print("Для обработки выбран JSON-файл\n")
            return get_list_of_operations("data/operations.json")
        elif data_choice == "2":
            print("Для обработки выбран CSV-файл\n")
            return get_data_from_csv("data/transactions.csv")
        elif data_choice == "3":
            print("Для обработки выбран XLSX-файл\n")
            return get_data_from_excel("data/transactions_excel.xlsx")
        else:
            print(
                """Выбран неверный пункт!\n
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
            )
            data_choice = input()


def get_filter_state(data):
    state = input(
        """Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
    )
    while True:
        if state.upper() == "EXECUTED":
            print('Операции отфильтрованы по статусу "EXECUTED"\n')
            filtered_data = filter_by_state(data, "EXECUTED")
            return filtered_data
        elif state.upper() == "CANCELED":
            print('Операции отфильтрованы по статусу "CANCELED"\n')
            filtered_data = filter_by_state(data, "CANCELED")
            return filtered_data
        elif state.upper() == "PENDING":
            print('Операции отфильтрованы по статусу "PENDING"\n')
            filtered_data = filter_by_state(data, "PENDING")
            return filtered_data
        else:
            print(f'Статус операции "{state}" недоступен.\n')
            state = input(
                """Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
            )


def is_need_sorting(data):
    is_sorted = input("Отсортировать операции по дате? Да/Нет\n")
    sorted_data = []
    if is_sorted.lower() == "да":
        sort_order = input("Отсортировать по возрастанию или по убыванию?\n")
        if sort_order.lower() == "по возрастанию":
            sorted_data = sort_by_date(data, False)
        elif sort_order.lower() == "по убыванию":
            sorted_data = sort_by_date(data, True)
    return sorted_data


def is_only_rub_transactions(data):
    is_rub_transactions = input("Выводить только рублевые транзакции? Да/Нет\n")
    rub_data = []

    if is_rub_transactions.lower() == "да":
        rub_data = list(filter_by_currency(data, "RUB"))

    return rub_data


def is_filtered_by_keyword(data):
    is_filtered_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    filtered_list_by_word = []

    if is_filtered_by_word.lower() == "да":
        filtered_word = input("Введите слово: ")
        filtered_list_by_word = filtered_by_query(data, filtered_word)

    return filtered_list_by_word


def get_summary(data):
    print("Распечатываю итоговый список транзакций...\n\n")

    if data:
        print(f"Всего банковских операций в выборке: {len(data)}\n")
        for item in data:
            print(f"{get_date(item['date'])} {item['description']}")
            if item.get("from"):
                print(f"{mask_account_card(item['from'])} -> {mask_account_card(item['to'])}")
            else:
                print(f"{mask_account_card(item['to'])}")

            if item.get("operationAmount"):
                print(f"Сумма: {item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}")
            else:
                print(f"Сумма: {item['amount']} {item['currency_name']}")
            print()
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
