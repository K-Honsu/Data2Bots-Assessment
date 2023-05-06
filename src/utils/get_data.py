import json


def get_data(data_path: str, key: str) -> dict:
    """loads data from a JSON file located at data_path and returns a dictionary associated with the specified key."""
    
    with open(data_path, 'r') as f:
        return json.load(f)[key]
