# import pytest
#
# from src.taxes import calculate_taxes
#
#
# def test_calculate_taxes():
# 	assert calculate_taxes([1, 2, 3], 1) == [1.01, 2.02, 3.03]
#
#
# def test_calculate_taxes_below_zero_tax_rate():
# 	with pytest.raises(ValueError) as exc_info:
# 		calculate_taxes([1, 2, 3], -2)
#
#
# def test_calculate_taxes_below_zero_prices():
# 	with pytest.raises(ValueError) as exc_info:
# 		calculate_taxes([1, -2, 3], 15)
import pytest

from src.taxes import calculate_tax


def test_calculate_tax_basic():
	assert calculate_tax(100, 10) == 110
	assert calculate_tax(50, 5) == 52.5


def test_calculate_tax_wrong_price():
	with pytest.raises(ValueError) as e:
		calculate_tax(-15, 10)


def test_calculate_tax_wrong_tax_rate():
	with pytest.raises(ValueError) as e:
		calculate_tax(250, -2)
		calculate_tax(250, 100)
		calculate_tax(250, 152)


def test_calculate_tax_no_discount():
	assert calculate_tax(100, 10, discount=0) == 110


def test_calculate_tax_with_discount():
	assert calculate_tax(100, 10, discount=10) == 99


def test_calculate_tax_round():
	assert calculate_tax(252, 14, discount=15, price_round=3) == 244.188
	assert calculate_tax(252, 14, discount=15, price_round=0) == 244
	assert calculate_tax(252, 14, discount=15) == 244.19


@pytest.mark.parametrize('price, tax_rate, discount, price_round', [
	('100', 10, 0, 1),
	(100, '10', 0, 1),
	(100, 10, '0', 1),
	(100, 10, 0, '1')
])
def test_calculate_tax_price_not_num(price, tax_rate, discount, price_round):
	with pytest.raises(TypeError):
		calculate_tax(price, tax_rate, discount=discount, price_round=price_round)


def test_calculate_tax_price_kwargs():
	with pytest.raises(TypeError):
		calculate_tax(100, 10, 2, 3)