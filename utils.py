import json

def load_data(file_path):
    data = []
    with open(file_path, "r") as file:
        for line in file:
            try:
                json_obj = json.loads(line)
                data.append(json_obj)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

    return data

def load_model_config(model_config_path):
    with open(model_config_path, "r") as config_file:
        config = json.load(config_file)
    return config
