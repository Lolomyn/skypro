import json
import codecs


def get_list_of_operations(path_to_file: str) -> list:
	with codecs.open(path_to_file, 'r', 'utf_8_sig') as json_file:
		operations = json.load(json_file)

	return operations


get_list_of_operations('data/operations.json')
