# Least-To-Most-Prompting

This project uses OpenAI's GPT-3.5 Turbo to solve mathematical word problems. It takes a set of prompts in the form of word problems, processes them using a predefined prompt structure, and provides answers based on the model's predictions.

## Usage

1. **Configure the Model**: Edit `config.json` to set the model parameters, API key, and file paths.

2. **Prepare Test Data**: Ensure your test data is in `data/test.jsonl` with questions and ground truth answers.

3. **Run the Main Script**: Execute `main.py` to load the model, process data, make predictions, and evaluate performance.

## Model Output

The model output, including predicted answers, will be stored in `output/answers.json` after each prediction.

## Evaluation

Model performance can be evaluated using metrics such as accuracy. The evaluation script is included in `utils.py`.

## Dependencies

- Python 3.x
- OpenAI GPT-3.5 Turbo API key

## Acknowledgments

This project is built on OpenAI's GPT-3.5 Turbo and follows the prompt-based appr
