from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils import markdown

from keyboards.common_keyboards import get_on_start_kb

router = Router(name=__name__)


@router.message(CommandStart())
async def cmd_start(message: types.Message):

    url = "https://nanojam.ru/userfiles/img/f0578e3b1a0382df16e64ef718954160.jpg"

    await message.answer(
        text=f"{markdown.hide_link(url)}Hello, {markdown.hbold(message.from_user.full_name)}!",
        reply_markup=get_on_start_kb(),
    )