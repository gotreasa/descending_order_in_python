def descending_order(number: int) -> int:
    if not isinstance(number, int):
        raise ValueError("❗️ Input should be a number")

    numbers = str(number)
    sorted_numbers = sorted([*numbers], reverse=True)
    full_number = "".join(sorted_numbers)
    return int(full_number)
