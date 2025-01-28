from src.main_utility import (
    get_filter_state,
    get_summary,
    get_user_output_format,
    is_filtered_by_keyword,
    is_need_sorting,
    is_only_rub_transactions
)


def main() -> None:
    """Консольное приложение по банковским операциям"""
    data = get_user_output_format()  # JSON, CSV или XLSX
    data = get_filter_state(data)  # EXECUTED, CANCELED или PENDING

    sorted_data = is_need_sorting(data)  # Нужна ли сортировка

    if sorted_data:
        data = sorted_data

    rub_data = is_only_rub_transactions(data)  # Только транзакции в рублях

    if rub_data:
        data = rub_data

    filtered_list_by_word = is_filtered_by_keyword(data)  # Фильтрация по ключевому слову

    if filtered_list_by_word:
        data = filtered_list_by_word

    get_summary(data)  # Вывод итоговой статистики


if __name__ == "__main__":
    main()
