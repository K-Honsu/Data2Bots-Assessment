from src.utils.get_types import get_data_types


def get_schema(data: dict) -> dict:
    '''takes in a dictionary data and returns a schema dictionary. '''
    
    schema = {}
    for key, values in data.items():
        value_types = get_data_types(values)
        schema[key] = {'type': value_types,
                       'tag': '', 'description': '', 'required': False}
    return schema
