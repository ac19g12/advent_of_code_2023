import numpy as np
import numpy.typing as npt
from util import Data

def part_a(text_input:npt.NDArray):
    array = []
    for line in text_input:
        line_break = [letter for letter in line]
        array.append(line_break)
    array = np.array(array)
    array_len = array.shape[1]
    array_width = array.shape[0]
    number = str()
    number_list = []
    symbol_gate = False
    for height in range(array_len):
        for width in range(array_width):
            centre = array[height, width]
            if centre.isnumeric():
                x = height - 1
                x = x if x>0 else 0
                y = height+2
                y = y if y<=array_len else array_len

                i = width-1
                i = i if i >0 else 0
                j = width + 2
                j = j if j<=array_width else array_width

                box = array[x:y,i:j]
                symbol_check = grid_search(box)
                if symbol_check:
                    symbol_gate = True
                number = number + centre
            else:
                if symbol_gate:
                    number_int = int(number)
                    number_list.append(number_int)
                number = str()
                symbol_gate = False
            
            if width == array_width-1:
                if symbol_gate:
                    number_int = int(number)
                    number_list.append(number_int)
                number = str()
                symbol_gate = False

    return sum(number_list)

def is_float(val) -> bool:
    try:
        float(val)
    except ValueError:
        return False
    return True

is_numeric = np.vectorize(is_float, otypes = [bool])

def grid_search(array:npt.NDArray) -> bool:
    a = array == "."
    b = is_numeric(array)
    c = (a + b)==False
    symbol_check = c.any()
    return symbol_check


def part_b(text_input: npt.NDArray):
    array = []
    for line in text_input:
        line_break = [letter for letter in line]
        array.append(line_break)
    array = np.array(array)
    print(array)
    a = array=="*"
    b = is_numeric(array)
    print(a|b)

if __name__ == "__main__":
    Day_3 = Data(3, data_file_type="py")
    score = part_a(Day_3.INPUT_1.to_array()) # type: ignore
    print(f"Day 3 part a: {score}")

    score_b = part_b(Day_3.TEST_1.to_array()) # type: ignore
    print(score_b)