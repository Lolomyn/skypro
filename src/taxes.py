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


def calculate_tax(price: float, tax_rate: float, *, discount=0, price_round=2):
    for arg in [price, tax_rate, discount, price_round]:
        if not isinstance(arg, (int, float)):
            raise TypeError("Ошибка типа данных")

    if price < 0:
        raise ValueError("Неверная цена")

    if tax_rate < 0 or tax_rate >= 100:
        raise ValueError("Неверный налоговый процент")

    if price_round == 0:
        return int((price + (tax_rate * price / 100)) * (1 - discount / 100))
    return round((price + (tax_rate * price / 100)) * (1 - discount / 100), price_round)
