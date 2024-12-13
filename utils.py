def reformat_from_str_to_list_octets(string: str) -> list[int | None]:
    """
    Преобразует строковое значение сети в список октетов.
    """
    octets = string.split('.')
    octets = list(map(lambda octet: int(octet) if 0 <= int(octet) <= 255 else None, octets))
    return octets
