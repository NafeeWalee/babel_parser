import ast
import json
import os

DIR = rf"{os.path.dirname(__file__)}"
py_DIR= rf"{DIR}\AtshaKeras_wildfireV2.py"
print(py_DIR)

def python_file_to_json(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()

    # Parse Python code into AST
    ast_tree = ast.parse(source_code)

    # Serialize AST to JSON
    json_data = ast.dump(ast_tree)

    return json_data


# Convert Python code from file to JSON
json_data = python_file_to_json(py_DIR)

# Print JSON data
print(json_data)

with open('py2json.json', 'w') as json_file:
        json.dump(json_data, json_file)