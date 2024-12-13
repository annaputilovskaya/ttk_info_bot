from aiogram.types import Message

from utils import reformat_from_str_to_list_octets


def valid_network_ip_filter(message: Message):
    """
    Проверяет возможность преобразования строки в список
    из четырех октетов в виде чисел и возвращает его.
    В случае невозможности преобразования ничего не возвращает.
    """
    if message.text:
        try:
            octets = reformat_from_str_to_list_octets(message.text)
            if len(octets) == 4 and None not in octets:
                return {"network": octets}
            return None
        except ValueError:
            return None

    return None
