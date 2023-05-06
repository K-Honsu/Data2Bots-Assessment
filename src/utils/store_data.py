import json


def dump_data(data: dict, data_path: str) -> None:
    '''takes in a dictionary data and dumps it into a JSON file located at data_path.'''

    with open(data_path, 'w') as f:
        return json.dump(data, f, indent=4)
