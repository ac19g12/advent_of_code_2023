import os
import yaml
from importlib.machinery import SourceFileLoader
import numpy as np
import numpy.typing as npt


class DataStr(str):
    def test(self):
        print(self)

    def to_list(self, new_line: str = " ") -> list:
        return self.split(new_line)

    def to_array(self, new_line: str = "\n") -> npt.NDArray:
        return np.array(self.to_list(new_line))

def find_modules(module: object) -> dict:
    names = [_name for _name in dir(module) if not ("__" in _name)]
    result_dict = {}
    for _var in names:
        result_dict[_var] = getattr(module, _var)
    return result_dict


class Data:
    def __init__(
        self,
        day: int,
        data_folder_name: str = "_data",
        data_prefrix: str = "day_",
        data_file_type: str = "yaml",
    ):
        base_path = os.getcwd()
        data_path = os.path.join(base_path, data_folder_name)

        file_nickname = f"{data_prefrix}{day}"
        file_name = f"{file_nickname}.{data_file_type}"
        file_path = os.path.join(data_path, file_name)

        if data_file_type == "yaml":
            with open(file_path, "r") as file:
                data = yaml.safe_load(file)
        elif data_file_type == "py":
            loader = SourceFileLoader(file_nickname, file_path)
            handle = loader.load_module(file_nickname)
            data = find_modules(handle)
        else:
            raise ValueError("No other data types allowed, only YAML")

        for key, value in data.items():
            self.__dict__[key] = DataStr(value.strip())

    @staticmethod
    def add_file(
        data: dict,
        day: int,
        data_folder_name: str = "_data",
        data_prefrix: str = "day_",
        data_file_type: str = "yaml",
    ) -> None:
        base_path = os.path.dirname(os.getcwd())
        data_path = os.path.join(base_path, data_folder_name)

        file_name = f"{data_prefrix}{day}.{data_file_type}"
        file_path = os.path.join(data_path, file_name)

        with open(file_path, "w") as file:
            if data_file_type == "yaml":
                yaml.dump(data, file, default_flow_style=False)
            else:
                raise ValueError("No other data types allowed, only YAML")

        return None


if __name__ == "__main__":
    Data(2, data_file_type="py")
