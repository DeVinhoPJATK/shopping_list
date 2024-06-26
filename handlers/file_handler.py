from models.list import List
import os
import json

STORAGE_DIRECTORY = 'data'

def init_data():
    if not os.path.exists(STORAGE_DIRECTORY):
        os.makedirs(STORAGE_DIRECTORY)

def load_lists():
    file_names = []
    for file_name in os.listdir(STORAGE_DIRECTORY):
        if file_name.endswith('.json'):
            file_name_without_extension = file_name[:-5]
            file_names.append(file_name_without_extension)
    return file_names

def create_list(list: List):
    list_dict = list.to_dict()
    file_path = build_file_path(list.name)
    with open(file_path, 'w') as file:
        json.dump(list_dict, file, indent=4)

def load_file_as_json(file_name: str):
    file_path = os.path.join(STORAGE_DIRECTORY, file_name + ".json")
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Plik {file_name} nie istnieje")
    with open(file_path, 'r') as file:
        return json.load(file)
    
def save(list: List):
    list_dict = list.to_dict()
    file_path = os.path.join(STORAGE_DIRECTORY, list.name + ".json")
    json_data = json.dumps(list_dict, indent=4)
    with open(file_path, 'w') as json_file:
        json_file.write(json_data)

def remove_file(file_name: str):
    file_path = build_file_path(file_name)
    if exists(file_name):
        os.remove(file_path)
        return True
    return False

def build_file_path(file_name: str):
    return os.path.join(STORAGE_DIRECTORY, file_name + ".json",)

def exists(file_name: str):
    return os.path.exists(build_file_path(file_name))