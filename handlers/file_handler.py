from models.list import List
import os
import json

STORAGE_DIRECTORY = 'data'

def load_lists():
    file_names = []
    for file_name in os.listdir(STORAGE_DIRECTORY):
        if file_name.endswith('.json'):
            file_name_without_extension = file_name[:-5]
            file_names.append(file_name_without_extension)
    return file_names

def load_file_as_json(file_name: str):
    file_path = os.path.join(STORAGE_DIRECTORY, file_name + ".json",)
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Plik {file_name} nie istnieje")
    with open(file_path, 'r') as file:
        return json.load(file)
    
def save(list: List):
    list_dict = list.to_dict()
    file_path = os.path.join(STORAGE_DIRECTORY, list.name + ".json",)
    json_data = json.dumps(list_dict, indent=4)
    with open(file_path, 'w') as json_file:
        json_file.write(json_data)