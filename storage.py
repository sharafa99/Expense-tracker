import json
from pathlib import Path

def load_storage(file_name):
    storage_path = Path(file_name)
    if storage_path.exists():

        with open(storage_path, "r") as file:
            return json.load(file)
    else:
        return {}


def save_expense(expenses, file_name ):
        
    with open(file_name, "w") as file:
        json.dump(expenses, file, indent=4)