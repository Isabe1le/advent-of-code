NUMBERS_AS_STRING = "0123456789"

with open("input.txt", "r") as file:
    input: str = file.read()

input_lines = input.split("\n")
current_total = 0

for line in input_lines:
    first_num: str | None = None
    last_num: str | None = None
    for char in line:
        if (
            char in NUMBERS_AS_STRING
            and first_num is None
        ):
            first_num = char
        elif char in NUMBERS_AS_STRING:
            last_num = char
    if (
        first_num is not None
        and last_num is not None
    ):
        num = int(first_num + last_num)
        current_total += num
    elif (
        first_num is not None
        and last_num is None
    ):
        num = int(first_num + first_num)
        current_total += num

print(current_total)
    