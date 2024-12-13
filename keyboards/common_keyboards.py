from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class ButtonText:
    """
    Названия кнопок меню.
    """
    SUBNET = "Параметры сети"
    HELP = "Все функции"
    CANCEL = "Отмена"


def get_on_start_kb() -> ReplyKeyboardMarkup:
    """
    Получает стартовую клавиатуру.
    """
    button_network = KeyboardButton(text=ButtonText.SUBNET)
    button_help = KeyboardButton(text=ButtonText.HELP)
    buttons_row = [button_network, button_help]
    markup = ReplyKeyboardMarkup(
        keyboard=[buttons_row,],
        resize_keyboard=True,
    )
    return markup
