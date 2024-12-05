from src.masks import get_mask_account, get_mask_card_number

CARD_NUMBER_STANDARD_LENGTH = 16
ACCOUNT_NUMBER_STANDARD_LENGTH = 20


def get_info() -> None:
    user_card_number = int(
        input("Добро пожаловать! Введите, пожалуйста, номер вашей карты (16 цифр), " "чтобы продолжить...\n")
    )
    if len(str(user_card_number)) == CARD_NUMBER_STANDARD_LENGTH:
        card_number_mask = get_mask_card_number(user_card_number)
        user_account_number = int(
            input(
                f"Отлично! Ваша карта {card_number_mask} существует, можем "
                f"продолжать.\nУкажите номер вашего счета (20 цифр), к которому привязана "
                f"указанная карта...\n"
            )
        )
        if len(str(user_account_number)) == ACCOUNT_NUMBER_STANDARD_LENGTH:
            account_number_mask = get_mask_account(user_account_number)
            print(
                f"Ваш счет {account_number_mask} принят.\n---\nВсе необходимые данные получены, спасибо, всего "
                f"доброго!"
            )
        else:
            print("Указанные вами данные неверны, попробуйте снова!\n---\n")
            get_info()
    else:
        print("Указанные вами данные неверны, попробуйте снова!\n---\n")
        get_info()


if __name__ == "__main__":
    get_info()
