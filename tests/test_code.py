# from src.code import hello
#
#
# def test_hello_normal():
# 	assert hello('World') == 'Hello World'
#
#
# def test_hello_blank():
# 	assert hello('') == ''
#
#
# def test_hello_numbers():
# 	assert hello(123) == 'Hello 123'
# from src.code import finder
#
#
# def test_finder_basic():
# 	assert finder([1, '2', [], {}, ('3',)], int) == 1
# 	assert finder([1, '2', [], {}, ('3',), 3], int) == 2
#
#
# def test_finder_zero_cur_type():
# 	assert finder([1, 2, [], {}, ('3',)], str) == 0
#
#
# def test_finder_zero_list():
# 	assert finder([], str) == 0
#
#
# def test_finder_not_list():
# 	assert finder(123, int) == 0
# import pytest
#
# from src.code import calculate_taxes
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
