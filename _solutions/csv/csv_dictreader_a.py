
result = []

with open(FILE, mode='rt') as file:
    reader = csv.DictReader(file)
    result = list(reader)
