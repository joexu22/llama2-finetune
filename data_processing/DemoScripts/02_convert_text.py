import json
import random

# Function to convert the content of answers.txt to the structure of novel17_eval.jsonl
def convert_to_jsonl(answers_content):
    jsonl_content = []
    for i in range(0, len(answers_content), 2):
        question = answers_content[i].strip()
        answer = answers_content[i + 1].strip() if i + 1 < len(answers_content) else ""
        jsonl_content.append(json.dumps({"text": f"### Human: {question} ### Assistant: {answer}"}))
    return jsonl_content

# Get the content of answers.txt
with open('test_answers.txt', 'r') as f:
    answers_content = f.readlines()

# Convert the content and write it to a new JSONL file
converted_jsonl = convert_to_jsonl(answers_content)
converted_jsonl_path = 'test_dataset.jsonl'

# Writes out intermediate jsonl file
with open(converted_jsonl_path, 'w') as f:
    for line in converted_jsonl:
        f.write(line + ',' + '\n')
