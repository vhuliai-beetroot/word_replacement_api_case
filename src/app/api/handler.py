from app.constants import REPLACEMENT_MAP


def process_input_string(input_str: str) -> str:
    """
    Process input string to replace certain words using config.

    :param input_str: input string to process
    :return new string object with replaced words.
    """
    for key, value in REPLACEMENT_MAP.items():
        input_str = input_str.replace(key, value)

    return input_str
