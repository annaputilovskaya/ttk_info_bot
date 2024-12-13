from keyboards.common_keyboards import ButtonText


def reformat_from_str_to_list_octets(string: str) -> list[int | None]:
    """
    Преобразует строковое значение сети в список октетов.
    """
    octets = string.split(".")
    octets = list(
        map(lambda octet: int(octet) if 0 <= int(octet) <= 255 else None, octets)
    )
    return octets


def get_network_info(network: str, prefix: str) -> dict | None:
    """
    Получает информацию о сети.
    """
    if prefix not in ButtonText.PREFIX:
        return None

    octets = reformat_from_str_to_list_octets(network)
    first_octets_str = ".".join(list(map(lambda octet: str(octet), octets[0:3])))
    ips_amount = 2 ** (32 - int(prefix))

    if (octets[3] + ips_amount) > 256:
        return None

    gateway_last_octet = str(octets[3] + 1)
    gateway = first_octets_str + "." + gateway_last_octet
    first_host_ip = f"{first_octets_str}.{str(octets[3] + 2)}"
    last_host_ip = f"{first_octets_str}.{str(octets[3] + ips_amount - 2)}"
    mask = f"{first_octets_str}.{str(256 - ips_amount)}"
    dns1 = "89.232.109.74"
    dns2 = "217.23.177.252"

    return {
        "gateway": gateway,
        "first_host_ip": first_host_ip,
        "last_host_ip": last_host_ip,
        "mask": mask,
        "dns1": dns1,
        "dns2": dns2,
    }
