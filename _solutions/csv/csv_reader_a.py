
result = []

with open(FILE, mode='r') as file:
    reader = csv.reader(file, lineterminator='\n')
    result = [tuple(x) for x in reader]
