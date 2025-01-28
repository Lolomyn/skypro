from unittest.mock import patch

from src.main_utility import get_filter_state, get_user_output_format, is_need_sorting, is_only_rub_transactions, \
    is_filtered_by_keyword, get_summary


def test_main_utility_get_user_output_format_json():
    with patch('builtins.input', return_value='1'):
        with patch('src.main_utility.get_list_of_operations', return_value=[{"id": 441945886}]):
            result = get_user_output_format()
            assert result == [{"id": 441945886}]


def test_main_utility_get_user_output_format_csv():
    with patch('builtins.input', return_value='2'):
        with patch('src.main_utility.get_data_from_csv', return_value=[{"id": 441945886}]):
            result = get_user_output_format()
            assert result == [{"id": 441945886}]


def test_main_utility_get_user_output_format_xlsx():
    with patch('builtins.input', return_value='3'):
        with patch('src.main_utility.get_data_from_excel', return_value=[{"id": 441945886}]):
            result = get_user_output_format()
            assert result == [{"id": 441945886}]


def test_main_utility_get_filter_state_executed(fixture_get_operations, fixture_executed_sort):
    user_input = ['executed']
    expected = fixture_executed_sort
    with patch('builtins.input', side_effect=user_input):
        result = get_filter_state(fixture_get_operations)
        assert result == expected


def test_main_utility_get_filter_state_canceled(fixture_get_operations, fixture_canceled_sort):
    user_input = ['canceled']
    expected = fixture_canceled_sort
    with patch('builtins.input', side_effect=user_input):
        result = get_filter_state(fixture_get_operations)
        assert result == expected


def test_main_utility_get_filter_state_pending(fixture_get_operations, ):
    user_input = ['pending']
    expected = []
    with patch('builtins.input', side_effect=user_input):
        result = get_filter_state(fixture_get_operations)
        assert result == expected


def test_main_utility_get_filter_state_two_inputs(fixture_get_operations, fixture_executed_sort):
    user_input = ['test', 'executed']
    expected = fixture_executed_sort
    with patch('builtins.input', side_effect=user_input):
        result = get_filter_state(fixture_get_operations)
        assert result == expected


def test_main_utility_is_need_sorting_sorted_up(fixture_get_operations, fixture_sorted_by_date_up):
    user_input = ['да', 'по возрастанию']
    expected = fixture_sorted_by_date_up

    with patch('builtins.input', side_effect=user_input):
        result = is_need_sorting(fixture_get_operations)
        assert result == expected


def test_main_utility_is_need_sorting_sorted_down(fixture_get_operations, fixture_sorted_by_date_down):
    user_input = ['да', 'по убыванию']
    expected = fixture_sorted_by_date_down

    with patch('builtins.input', side_effect=user_input):
        result = is_need_sorting(fixture_get_operations)
        assert result == expected


def test_main_utility_is_need_sorting_not_sorted(fixture_get_operations):
    user_input = ['нет']
    expected = []

    with patch('builtins.input', side_effect=user_input):
        result = is_need_sorting(fixture_get_operations)
        assert result == expected


def test_main_utility_is_only_rub_transactions_true(fixture_get_operations, fixture_sorted_by_rub):
    user_input = ['да']
    expected = fixture_sorted_by_rub

    with patch('builtins.input', side_effect=user_input):
        result = is_only_rub_transactions(fixture_get_operations)
        assert result == expected


def test_main_utility_is_only_rub_transactions_false(fixture_get_operations):
    user_input = ['нет']
    expected = []

    with patch('builtins.input', side_effect=user_input):
        result = is_only_rub_transactions(fixture_get_operations)
        assert result == expected


def test_main_utility_is_filtered_by_keyword_true(fixture_get_operations, fixture_sorted_by_keyword):
    user_input = ['Да', 'вклад']
    expected = fixture_sorted_by_keyword

    with patch('builtins.input', side_effect=user_input):
        result = is_filtered_by_keyword(fixture_get_operations)
        assert result == expected


def test_main_utility_is_filtered_by_keyword_false(fixture_get_operations):
    user_input = ['нет']
    expected = []

    with patch('builtins.input', side_effect=user_input):
        result = is_filtered_by_keyword(fixture_get_operations)
        assert result == expected


def test_main_utility_get_summary(capsys, fixture_for_summary):
    get_summary(fixture_for_summary)
    captured = capsys.readouterr()
    assert captured.out == 'Распечатываю итоговый список транзакций...\n\n\n' \
                           'Всего банковских операций в выборке: 1\n\n' \
                           '26.08.2019 Перевод организации\n' \
                           'Maestro 1596 83** **** 5199 -> Счет **9589\n' \
                           'Сумма: 31957.58 руб.\n\n'


def test_main_utility_get_summary_empty(capsys):
    get_summary([])
    captured = capsys.readouterr()
    assert captured.out == 'Распечатываю итоговый список транзакций...\n\n\n' \
                           'Не найдено ни одной транзакции, подходящей под ваши условия фильтрации\n'


def test_main_utility_get_summary_without_from(capsys, fixture_for_summary_without_from):
    get_summary(fixture_for_summary_without_from)
    captured = capsys.readouterr()
    assert captured.out == 'Распечатываю итоговый список транзакций...\n\n\n' \
                           'Всего банковских операций в выборке: 1\n\n' \
                           '26.08.2019 Перевод организации\n' \
                           'Счет **9589\n' \
                           'Сумма: 31957.58 руб.\n\n'
