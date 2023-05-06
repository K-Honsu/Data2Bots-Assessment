# Data2Bots-Assessment <hr>

- This is a Python program that reads a JSON file, sniffs the data from the JSON file and dumps the output in the desired directory.

## How to setup <hr>

1. Clone the repository - git clone https://github.com/K-Honsu/Data2Bots-Assessment.git
2. Navigate to the root folder of the project in your terminal.
3. Run the command below to execute the script.

```
python main.py
```

## How it works <hr>

- src/utils/get_data.py -> get_data(data_path: str, key: str) -> dict: This function takes a file path and a key argument and returns a dictionary with the value of the specified key from a JSON file at the given file path.
- src/utils/get_schema.py -> get_schema(data): This function takes a dictionary as an argument and returns the required schema that describes the data types of the dictionary's keys.
- src/utils/get_types.py -> get_types(value): This function takes a value as an argument and returns a string indicating the data type of that value. The data type is determined using the built-in type function and a dictionary mapping data types to their string representation.
- src/utils/store_data.py -> dump_data(data, data_path: str): This function takes a dictionary and a file path as arguments and writes the dictionary to a JSON file at the specified path. The data is formatted with an indent of 4 spaces.

## How to run tests <hr>

1. Navigate to the project directory in the terminal/command prompt by running the following command

   - ```
     python test.py
     ```

2. View the test results in the terminal/command prompt
