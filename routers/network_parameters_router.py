from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from filters.network_parameters_filters import valid_network_ip_filter
from keyboards.common_keyboards import ButtonText, get_prefix_kb, get_on_start_kb
from routers.states import NetworkParameters
from utils import get_network_info

router = Router(name=__name__)


@router.message(F.text == ButtonText.SUBNET)
@router.message(Command("subnet", prefix="!/"))
async def start_get_network_parameters(message: Message, state: FSMContext):
    await state.set_state(NetworkParameters.network_ip)
    await message.answer(
        text="Укажите  IP сети в формате 255.255.255.255",
    )


@router.message(NetworkParameters.network_ip, valid_network_ip_filter)
async def handle_valid_network_ip(
    message: Message,
    state: FSMContext,
):
    await state.update_data(network=message.text)
    await state.set_state(NetworkParameters.prefix)
    await message.answer(
        text="Выберите префикс (битность сети) или отмените ввод:",
        reply_markup=get_prefix_kb(),
    )


@router.message(NetworkParameters.network_ip)
async def handle_invalid_network_ip(message: Message):
    await message.answer(
        "Некорректный формат IP сети. Пожалуйста, введите текст в формате 255.255.255.255",
    )


@router.message(NetworkParameters.prefix, F.text == ButtonText.CANCEL)
async def handle_prefix_cancel(
    message: Message,
    state: FSMContext,
):
    await state.clear()
    await message.answer(text="Отмена ввода", reply_markup=get_on_start_kb())


@router.message(NetworkParameters.prefix, F.text)
async def handle_text_prefix(
    message: Message,
    state: FSMContext,
):
    data = await state.update_data(prefix=message.text)
    info = get_network_info(data["network"], data["prefix"])
    await state.clear()
    if info:
        await message.answer(
            text=f'Сеть: {data["network"]} / {data["prefix"]}\n'
            f'Шлюз: {info["gateway"]}\n'
            f'IP первого хоста: {info["first_host_ip"]}\n'
            f'IP последнего хоста: {info["last_host_ip"]}\n'
            f'Маска: {info["mask"]}\n'
            f'DNS1: {info["dns1"]}\n'
            f'DNS2: {info["dns2"]}\n',
            reply_markup=get_on_start_kb(),
        )
    else:
        await message.answer(
            text=f"Сеть с IP {data["network"]} и префиксом {data["prefix"]} в ТТК не существует. "
            f"Проверьте корректность данных.",
            reply_markup=get_on_start_kb(),
        )
