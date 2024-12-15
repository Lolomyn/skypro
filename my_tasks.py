# from typing import Any, List
#
#
# def list_intersection(list_1: List[int], list_2: List[int]) -> List[int]:
#     """Функция, которая возвращает новый список, содержащий значения, которые встречаются в обоих списках"""
#     return list(set.intersection(set(list_1), set(list_2)))
#
#
# print(list_intersection([1, 2, 3, 4], [3, 4, 5, 6]))
#
#
# def is_palindrome(check_list: List[int]) -> List[int]:
#     """Функция, которая возвращает список, состоящий из палиндромов"""
#     return [x for x in check_list if str(x)[::] == str(x)[::-1]]
#
#
# print(is_palindrome([121, 123, 131, 34543]))
#
#
# def list_union(list_1: List[int], list_2: List[int]) -> List[int]:
#     """Функция, которая возвращает новый список, содержащий значения, которые встречаются в обоих списках"""
#     return list(set(list_1) - set(list_2)) + list(set(list_2) - set(list_1))
#
#
# print(list_union([1, 2, 3, 4], [3, 4, 5, 6]))
#
#
# def calculate_circle_area(r: int) -> float:
#     pi = 3.14
#     circle_area = pi * r**2
#     return circle_area
#
#
# def format_description(r: int, area: float) -> Any:
#     return "Radius is " + str(r) + "; area is " + str(round(area, 2))
#
#
# def get_info(r: int) -> None:
#     area = calculate_circle_area(r)
#     description = format_description(r, area)
#     print(description)
#
#
# radius = int(input("Enter circle radius (int): "))
# get_info(radius)
