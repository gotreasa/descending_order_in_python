def sort_descending(number: str) -> list[str]:
    return sorted([*number], reverse=True)


def character_to_string(characters: list[str]) -> str:
    return "".join(characters)


def descending_order(number: int) -> int:
    if not isinstance(number, int):
        raise ValueError("❗️ Input should be a number")

    if number < 1:
        raise ValueError("❗️ Input should be a positive integer")

    number = str(number)
    sorted_numbers = sort_descending(number)
    full_number = character_to_string(sorted_numbers)
    return int(full_number)
