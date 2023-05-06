from src.utils.get_types import get_data_types
from src.utils.get_data import get_data
from src.utils.get_schema import get_schema
import unittest


class TestScenario(unittest.TestCase):
    def test_string_values(self):
        data = 'abc'
        result = get_data_types(data)
        self.assertEqual(result, 'string')

    def test_integer_values(self):
        data = 123
        result = get_data_types(data)
        self.assertEqual(result, 'integer')

    def test_empty_data(self):
        data = []
        result = get_data_types(data)
        self.assertEqual(result, 'array')

    def test_enum_type(self):
        result = get_data_types(["foo", "bar", "baz"])
        self.assertEqual(result, "enum")

    def test_object_type(self):
        result = get_data_types({"name": "John", "age": 30})
        self.assertEqual(result, "object")

    def test_empty_object_type(self):
        result = get_data_types({})
        self.assertEqual(result, "object")

    def test_boolean_type(self):
        result = get_data_types(True)
        self.assertEqual(result, "boolean")

    def test_schema_is_valid(self):
        data = get_data('src/data/test_data.json', 'message')
        result = {

            "battle": {
                "type": "object",
                "tag": "",
                "description": "",
                "required": False
            },

        }
        self.assertEqual(result, get_schema(data))


if __name__ == '__main__':
    unittest.main()
