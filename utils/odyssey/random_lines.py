import random

input_file = "pg1727.txt"
output_file = "random.txt"

with open(input_file, "r", encoding="utf-8") as f:
    words = set(f.read().split())  # Create a set of unique words

word_list = list(words)  # Convert to list for random selection

# Generate lines of ~1KB (1024 bytes)
num_lines = 1_000_000
target_size = 1024  # 1KB per line

with open(output_file, "w", encoding="utf-8") as f:
    for _ in range(num_lines):
        line_words = []
        line_length = 0

        while line_length < target_size:
            word = random.choice(word_list)
            line_words.append(word)
            line_length += len(word) + 1  # +1 for space

        f.write(" ".join(line_words) + "\n")  # Write to file
