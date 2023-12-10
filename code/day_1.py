from util import Data

Day_1 = Data(1)


# %% Part A
def part_a(text_input: list) -> int:
    result = 0
    for line in text_input:
        numbers = [letter for letter in line if letter.isnumeric()]
        text_value = numbers[0] + numbers[-1]
        result += int(text_value)
    return result


# %% Part B
NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def replace_str_index(text, index=0, replacement=""):
    return f"{text[:index]}{replacement}{text[index+1:]}"


def part_b(test_input: list) -> int:
    new_text = []
    for line in test_input:
        pos = [line.find(key) for key in NUMBERS]
        pos_filter = [_p for _p in pos if _p >= 0]
        if pos_filter:
            _min_p = min(pos_filter)
            min_value = [_v for _v, _p in zip(NUMBERS, pos) if _p == _min_p][0]
            line = replace_str_index(line, _min_p, NUMBERS[min_value])

        pos = [line.rfind(key) for key in NUMBERS]
        pos_filter = [_p for _p in pos if _p >= 0]
        if pos_filter:
            _max_p = max(pos_filter)
            max_value = [_v for _v, _p in zip(NUMBERS, pos) if _p == _max_p][0]

            line = replace_str_index(line, _max_p, NUMBERS[max_value])
        new_text.append(line)
    return part_a(new_text)


# %% Running Code
if __name__ == "__main__":
    score_a = part_a(Day_1.INPUT_1.to_list()) # type: ignore
    print(f"day 1 part a: {score_a}")

    score_b = part_b(Day_1.INPUT_1.to_list()) # type: ignore
    print(f"day 1 part b: {score_b}")
