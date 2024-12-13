from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.common_keyboards import ButtonText
from routers.states import NetworkParameters

router = Router(name=__name__)


@router.message(F.text == ButtonText.SUBNET)
@router.message(Command("subnet", prefix="!/"))
async def start_get_network_parameters(message: Message, state: FSMContext):
    await state.set_state(NetworkParameters.network_ip)
    await message.answer(
        "Укажите  IP сети в формате 255.255.255.255",
    )