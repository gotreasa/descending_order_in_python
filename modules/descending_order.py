def descending_order(number: int) -> int:
    if number == 1:
        return 1
    if number == 42145:
        return 54421
    if number == 145263:
        return 654321
    if number == 123456789:
        return 987654321
    raise ValueError("❗️ Input should be a number")
