import numpy as np
import numpy.typing as npt
from util import Data


# RGB
def game_data_counter(game_data: list) -> list:
    data = {"red": 0, "green": 0, "blue": 0}
    for line in game_data:
        for cube in line.split(","):
            values = cube.strip().split(" ")
            if data[values[1]] < int(values[0]):
                data[values[1]] = int(values[0])
    return [data["red"], data["green"], data["blue"]]

def cube_array_generator(text_input:list) -> npt.NDArray:
    array = np.empty((len(text_input),4))
    for line in text_input:
        game_index = line.find(":")
        index = int(line[5:game_index])
        game_data = line[game_index + 1 :]
        rgb = game_data_counter(game_data.split(";"))
        array[index-1] = [index, *rgb]
    return array

def part_a(text_input: list) -> int:
    array = cube_array_generator(text_input)
    r_mask = array[:, 1] <= 12
    g_mask = array[:, 2] <= 13
    b_mask = array[:, 3] <= 14
    total_mask = r_mask & g_mask & b_mask
    filter_games_id = array[total_mask, 0]
    return int(sum(filter_games_id))

def part_b(text_input:list) -> int:
    array = cube_array_generator(text_input)
    prod_array = np.prod(array[:,1:], axis=1)
    return int(sum(prod_array))


if __name__ == "__main__":
    Day_2 = Data(2, data_file_type="py")

    score = part_a(Day_2.INPUT_1.to_list("\n")) # type: ignore
    print(f"Day 2 part a: {score}")

    score_b = part_b(Day_2.INPUT_1.to_list("\n"))
    print(f"Day 2 part b: {score_b}")