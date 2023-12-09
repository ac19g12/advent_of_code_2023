import os
import yaml

class DataStr(str):
    def test(self):
        print(self)

    def to_list(self):
        return self.split(" ")

class Data():
    def __init__(self,
                 day:int,
                 data_folder_name:str="_data",
                 data_prefrix:str="day_",
                 data_file_type:str="yaml"):

        base_path = os.path.dirname(os.getcwd())
        data_path = os.path.join(base_path, data_folder_name)

        file_name = f"{data_prefrix}{day}.{data_file_type}"
        file_path = os.path.join(data_path, file_name)

        with open(file_path, 'r') as file:
            if data_file_type == "yaml":
                data = yaml.safe_load(file)
            else:
                raise ValueError("No other data types allowed, only YAML")

        for key, value in data.items():
            self.__dict__[key] = DataStr(value.strip())

    @staticmethod
    def add_file(data:dict, 
                 day:int,
                 data_folder_name:str="_data",
                 data_prefrix:str="day_",
                 data_file_type:str="yaml") -> None:
        
        base_path = os.path.dirname(os.getcwd())
        data_path = os.path.join(base_path, data_folder_name)

        file_name = f"{data_prefrix}{day}.{data_file_type}"
        file_path = os.path.join(data_path, file_name)

        with open(file_path, 'w') as file:
            if data_file_type == "yaml":
                data = yaml.dump(data, file, default_flow_style=False)
            else:
                raise ValueError("No other data types allowed, only YAML")

        return None
    