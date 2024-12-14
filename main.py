from src.widget import get_date, mask_account_card

CARD_NUMBER_STANDARD_LENGTH = 16
ACCOUNT_NUMBER_STANDARD_LENGTH = 20


def get_info() -> None:
    user_card_number = input(
        "Добро пожаловать! Введите, пожалуйста, " "номер вашей карты (16 цифр), чтобы продолжить...\n"
    )
    card_number_mask = mask_account_card(user_card_number)
    user_account_number = input(
        f"Отлично! Ваша карта {card_number_mask} существует, можем "
        f"продолжать.\nУкажите номер вашего счета (20 цифр), к которому привязана "
        f"указанная карта...\n"
    )
    account_number_mask = mask_account_card(user_account_number)
    print(f"Ваш счет {account_number_mask} принят.\n---\nВсе необходимые данные получены, спасибо, всего " f"доброго!")
    print(f'Дата вашего визита: {get_date("2024-05-12T21:49:52.671407")}')


if __name__ == "__main__":
    get_info()

# some changes
