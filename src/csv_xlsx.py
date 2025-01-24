import csv

import pandas as pd


def get_data_from_csv(path_to_csv_file: str) -> list[dict]:
    """Преобразует данные из csv файла в список словарей Python"""
    result_dict = []

    with open(path_to_csv_file, encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            result_dict.append({
                'id': row['id'],
                'state': row['state'],
                'date': row['date'],
                'amount': row['amount'],
                'currency_name': row['currency_name'],
                'currency_code': row['currency_code'],
                'from': row['from'],
                'to': row['to'],
                'description': row['description']
            })
    return result_dict


def get_data_from_excel(path_to_excel_file: str) -> list[dict]:
    """Преобразует данные из excel файла в список словарей Python"""
    excel_data = pd.read_excel(path_to_excel_file).to_dict(orient='records')
    return excel_data
