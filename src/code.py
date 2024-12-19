# def hello(word):
# 	if word:
# 		return f'Hello {word}'
# 	else:
# 		return ''
#
#
# def finder(my_list, my_type):
# 	counter = 0
# 	if isinstance(my_list, list):
# 		for item in my_list:
# 			if isinstance(item, my_type):
# 				counter += 1
# 	return counter


# def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
#     """Функция вычисляет стоимость товаров с учётом налога."""
#
#     if tax_rate < 0:
#         raise ValueError('Неверный налоговый процент')
#
#     taxed_prices = []
#
#     for price in prices:
#         if price <= 0:
#             raise ValueError('Неверная цена')
#         tax = price * tax_rate / 100
#         taxed_prices.append(price + tax)
#
#     return taxed_prices
