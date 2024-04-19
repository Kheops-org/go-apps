import sys
from ruamel.yaml import YAML

def update_yaml(file_path, path_to_update, new_value):
    yaml = YAML()
    yaml.preserve_quotes = True  # Optional, to preserve the original quotation marks

    # Load the YAML file
    with open(file_path, 'r') as file:
        data = yaml.load(file)

    # Split the path to navigate through the YAML structure
    keys = path_to_update.strip('.').split('.')
    # Access the nested dictionary and update the value
    temp = data
    for key in keys[:-1]:
        temp = temp[key]
    temp[keys[-1]] = new_value

    # Write the YAML file back
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python update_yaml.py <path/to/file.yaml> <.path.to.key> <new_value>")
        sys.exit(1)

    file_path = sys.argv[1]
    path_to_update = sys.argv[2]
    new_value = sys.argv[3]

    update_yaml(file_path, path_to_update, new_value)

