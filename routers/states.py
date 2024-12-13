from aiogram.fsm.state import StatesGroup, State


class NetworkParameters(StatesGroup):
    """
    Состояния получения параметров сети.
    """

    network_ip = State()
    prefix = State()
