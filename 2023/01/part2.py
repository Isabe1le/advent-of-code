NUMBERS_AS_STRING = "0123456789"
NUMBERS_AS_WORDS_TO_STRING = {
    "one": "o1e",
    "two": "t2o",
    "three": "th3ee",
    "four": "f4ur",
    "five": "f5ve",
    "six": "s6x",
    "seven": "se7en",
    "eight": "ei8ht",
    "nine": "n9ne"
}

with open("input.txt", "r") as file:
    input: str = file.read()

# Doesn't work for edge-cases such as "eightwo" -> "8ow" not "eigh2".
# for str_name, str_num in NUMBERS_AS_WORDS_TO_STRING.items():
#     input = input.replace(str_name, str_num)

input_lines = input.split("\n")
current_total = 0

for line in input_lines:
    line_cleaned = ""
    for char in line:
        line_cleaned += char
        for str_name, str_num in NUMBERS_AS_WORDS_TO_STRING.items():
            line_cleaned = line_cleaned.replace(str_name, str_num)

    first_num: str | None = None
    last_num: str | None = None
    for char in line_cleaned:
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
    