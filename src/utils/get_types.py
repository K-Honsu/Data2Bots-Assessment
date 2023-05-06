def get_data_types(value: any) -> str:
    '''takes in a value and returns the data type of the value.'''

    data_types = {str: 'string', int: 'integer', list: 'array',
                  dict: 'object', bool: 'boolean'}
    if isinstance(value, list):
        if not len(value):
            return 'array'
        if isinstance(value[0], str):
            return 'enum'

    return data_types[type(value)]
