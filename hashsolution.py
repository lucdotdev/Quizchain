import csv
import hashlib

def generate_md5_hash(solution_string):
    md5_hash = hashlib.md5()
    md5_hash.update(solution_string.encode('utf-8'))
    return md5_hash.hexdigest()

# Assuming the CSV file has a column named 'solution'
csv_file_path = 'solutions.csv'


if __name__ == '__main__':
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            md5_hash = generate_md5_hash(row)
            print(md5_hash)
