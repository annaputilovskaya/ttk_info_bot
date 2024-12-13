from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from filters.network_parameters_filters import valid_network_ip_filter
from keyboards.common_keyboards import ButtonText, get_prefix_kb
from routers.states import NetworkParameters

router = Router(name=__name__)


@router.message(F.text == ButtonText.SUBNET)
@router.message(Command("subnet", prefix="!/"))
async def start_get_network_parameters(message: Message, state: FSMContext):
    await state.set_state(NetworkParameters.network_ip)
    await message.answer(
        "Укажите  IP сети в формате 255.255.255.255",
    )


@router.message(NetworkParameters.network_ip, valid_network_ip_filter)
async def handle_valid_network_ip(
        message: Message,
        state: FSMContext,
):
    await state.update_data(network=message.text)
    await state.set_state(NetworkParameters.prefix)
    await message.answer(
        "Выберите префикс (битность сети) или отмените ввод:",
        reply_markup=get_prefix_kb(),
    )


@router.message(NetworkParameters.network_ip)
async def handle_invalid_network_ip(
        message: Message
):
    await message.answer(
        "Некорректный формат IP сети. Пожалуйста, введите текст в формате 255.255.255.255",
    )
