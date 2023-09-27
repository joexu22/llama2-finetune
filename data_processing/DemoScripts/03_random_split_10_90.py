import random
from math import ceil

# Read the converted JSONL file
with open('test_dataset.jsonl', 'r') as f:
    all_lines = f.readlines()

# Calculate the number of lines for each split
total_lines = len(all_lines)

# Shuffle the lines randomly
random.shuffle(all_lines)

# Calculate the number of lines for each random split
# The percentages (10% and 90%) remain the same
num_lines_10_percent_random = ceil(total_lines * 0.10)
num_lines_90_percent_random = total_lines - num_lines_10_percent_random

# Split the lines
lines_10_percent_random = all_lines[:num_lines_10_percent_random]
lines_90_percent_random = all_lines[num_lines_10_percent_random:]

# Write the random splits to new files
path_10_percent_random = 'test_eval_10_percent_random.jsonl'
path_90_percent_random = 'test_train_90_percent_random.jsonl'

with open(path_10_percent_random, 'w') as f:
    f.writelines(lines_10_percent_random)

with open(path_90_percent_random, 'w') as f:
    f.writelines(lines_90_percent_random)
