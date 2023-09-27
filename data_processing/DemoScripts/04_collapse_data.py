def collapse_file(input_file, output_file):
    """
    Read a file, remove newlines and tabs, and write it back to another file.

    Parameters:
    - input_file (str): The name of the input file.
    - output_file (str): The name of the output file.
    """
    with open(input_file, 'r') as in_f, open(output_file, 'w') as out_f:
        content = in_f.read()
        collapsed_content = content.replace('\n', '').replace('\t', '')
        out_f.write(collapsed_content)

if __name__ == '__main__':
    # Collapse 10% eval dataset
    collapse_file('test_eval_10_percent_random.jsonl', 'test_dataset_eval.jsonl')

    # Collapse 90% train dataset
    collapse_file('test_train_90_percent_random.jsonl', 'test_dataset_train.jsonl')
