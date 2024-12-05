import masks


def mask_account_card(user_data: str) -> str:
	"""Функция, которая принимает номер карты или счета и возвращает его замаскированным"""
	return masks.get_mask_account(user_data.split()[-1]) if len(user_data.split()[-1]) == 20 \
		else masks.get_mask_card_number(user_data.split()[-1])


# print(mask_account_card("Счет 73654108430135874305"))


def get_date(cur_date: str) -> str:
	"""Функция, которая принимает дату в формате "2024-03-11T02:26:18.671407" возвращает строку в формате ДД.ММ.ГГГГ"""
	return f"{cur_date[:10].split('-')[2]}.{cur_date[:10].split('-')[1]}.{cur_date[:10].split('-')[0]}"


# print(get_date("2024-03-11T02:26:18.671407"))
