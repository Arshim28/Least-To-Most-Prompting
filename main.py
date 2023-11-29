import json
from model import Model
from utils import load_data, evaluate

def main():
    model_config_path = "config.json"
    model = Model(model_config_path)

    existing_answers_path = "output/answers.json"
    existing_answers = load_data(existing_answers_path)

    test_data_path = "data/test.jsonl"
    test_data = load_data(test_data_path)

    last_processed_index = len(existing_answers)

    answers = []

    for example_dict in test_data[last_processed_index:]:
        output = model.predict(example_dict)
        answers.append(output)

        with open(existing_answers_path, "w") as output_file:
            json.dump(answers, output_file, indent=2)

    ground_truth_path = "data/test.jsonl"
    ground_truth = load_data(ground_truth_path)

    accuracy = evaluate(answers, ground_truth)
    
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    main()
