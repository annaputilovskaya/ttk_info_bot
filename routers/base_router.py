from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils import markdown

from keyboards.common_keyboards import get_on_start_kb, ButtonText

router = Router(name=__name__)


@router.message(CommandStart())
async def cmd_start(message: Message):
    """
    Обрабатывает команду старт.
    Выводит картинку, приветствие по полному имени пользователя и стартовое меню.
    """
    url = "https://nanojam.ru/userfiles/img/f0578e3b1a0382df16e64ef718954160.jpg"

    await message.answer(
        text=f"{markdown.hide_link(url)}Hello, {markdown.hbold(message.from_user.full_name)}!",
        reply_markup=get_on_start_kb(),
    )


@router.message(Command("help"))
async def cmd_help(message: Message):
    """
    Обрабатывает команду помощь.
    Выводит стартовое меню.
    """
    await message.answer(text="Чем могу помочь?", reply_markup=get_on_start_kb())


@router.message(F.text == ButtonText.OTHER)
async def handle_other(
    message: Message,
):
    """
    Обрабатывает другие функции.
    """
    await message.answer(
        text="Другие функции пока в разработке", reply_markup=get_on_start_kb()
    )


@router.message()
async def handle_unknown_input(message: Message):
    """
    Обрабатывает неизвестный ввод.
    Выводит стартовое меню.
    """
    await message.answer(
        text=markdown.text(
            "Неизвестный запрос. Пожалуйста, выберите необходимую функцию меню. "
            "Если меню не отображается, введите команду ",
            markdown.hbold("/help"),
        ),
        reply_markup=get_on_start_kb(),
    )
