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

def evaluate(predictions, ground_truth):
    correct_count = 0
    total_count = len(ground_truth)

    for prediction, truth in zip(predictions, ground_truth):
        predicted_answer = prediction["answer"]
        true_answer = truth["answer"]

        if predicted_answer == true_answer:
            correct_count += 1

    accuracy = correct_count / total_count
    return accuracy
