from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class ButtonText:
    """
    Названия кнопок меню.
    """

    SUBNET = "Параметры сети"
    HELP = "Все функции"
    CANCEL = "Отмена"
    PREFIX = [
        "26",
        "27",
        "28",
        "29",
        "30",
    ]


def get_on_start_kb() -> ReplyKeyboardMarkup:
    """
    Получает стартовую клавиатуру.
    """
    button_network = KeyboardButton(text=ButtonText.SUBNET)
    button_help = KeyboardButton(text=ButtonText.HELP)
    buttons_row = [button_network, button_help]
    markup = ReplyKeyboardMarkup(
        keyboard=[
            buttons_row,
        ],
        resize_keyboard=True,
    )
    return markup


def get_prefix_kb() -> ReplyKeyboardMarkup:
    """
    Получает клавиатуру префиксов сети (битности).
    """

    builder = ReplyKeyboardBuilder()
    for prefix in ButtonText.PREFIX:
        builder.add(KeyboardButton(text=prefix))
    builder.row(KeyboardButton(text="Отмена"))
    return builder.as_markup(resize_keyboard=True)
