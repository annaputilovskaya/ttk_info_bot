from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


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


def get_prefix_kb() -> ReplyKeyboardMarkup:
    """
    Получает клавиатуру префиксов сети (битности).
    """
    bit_rates = [
        "26",
        "27",
        "28",
        "29",
        "30",
    ]
    builder = ReplyKeyboardBuilder()
    for bit_rate in bit_rates:
        builder.add(KeyboardButton(text=bit_rate))
    builder.row(KeyboardButton(text="Отмена"))
    return builder.as_markup(resize_keyboard=True)
