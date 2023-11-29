import json
from model import Model
from utils import load_data

def main():
    model_config_path = "config.json"
    model = Model(model_config_path)

    data_path = "data/test.jsonl"
    data = load_data(data_path)

    answers = []

    for example_dict in data:
        output = model.predict(example_dict)
        answers.append(output)

        output_path = "output/answers.json"
        with open(output_path, "w") as output_file:
            json.dump(answers, output_file, indent=2)

    ground_truth_path = "data/test.jsonl"
    ground_truth = load_data(ground_truth_path)

    accuracy = evaluate(answers, ground_truth)
    
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    main()
