import csv

with open('r-m-c.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))

with open('rmc.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))

compared_files = ['r-m-c.csv', 'rmc.csv']
non_repeating_lines = set()
header_saved_once = False

with open('result_homework_15.csv', 'w', encoding='utf-8') as out_file:
    for filename in compared_files:
        with open(filename, 'r', encoding='utf-8') as in_file:
            header = next(in_file)
            if not header_saved_once:
                out_file.write(header)
                header_saved_once = True

            for line in in_file:
                if line not in non_repeating_lines:
                    out_file.write(line)
                    non_repeating_lines.add(line)

print("Files merged, duplicates removed!")
