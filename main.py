from src.utils.get_data import get_data
from src.utils.get_schema import get_schema
from src.utils.store_data import dump_data

data_paths = ['src/data/data_1.json', 'src/data/data_2.json']
output_paths = ['src/schema/schema_1.json', 'src/schema/schema_2.json']

if __name__ == '__main__':
    for i in range(len(data_paths)):
        data = get_data(data_paths[i], 'message')
        # print(data)
        schema = get_schema(data)
        # print(schema)
        dump = dump_data(schema, output_paths[i])
