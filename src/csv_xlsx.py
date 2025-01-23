import csv
import pandas as pd


def get_data_from_csv(path_to_csv_file):
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


# debug
# transactions_from_csv = get_data_from_csv('data/transactions.csv')
# print(transactions_from_csv[0])
#

def get_data_from_excel(path_to_excel_file):
    excel_data = pd.read_excel(path_to_excel_file).to_dict(orient='records')
    return excel_data

# debug
# transactions_from_excel = get_data_from_excel('data/transactions_excel.xlsx')
# print(transactions_from_excel[0])
