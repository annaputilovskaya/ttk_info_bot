from aiogram.types import Message

from utils import reformat_from_str_to_list_octets


def valid_network_ip_filter(message: Message):
    try:
        octets = reformat_from_str_to_list_octets(message.text)
        if len(octets) == 4 and None not in octets:
            return {"network": octets}
        return None
    except TypeError:
        return None
