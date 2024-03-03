def count_lines(file_name):
    with open(file_name, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
            return line_count
file_name = "sample.txt"
lines_count = count_lines(file_name)
print(f"Number of lines in '{file_name}': {lines_count}")
