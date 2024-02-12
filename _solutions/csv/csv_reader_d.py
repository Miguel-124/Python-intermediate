
result = []

with open(FILE, mode='r') as file:
    header = file.readline().strip().split(',')
    result.append(tuple(header))
    reader = csv.reader(file, lineterminator='\n')

    for *features, label in reader:
        features = [float(x) for x in features]
        row = features + [label]
        result.append(tuple(row))
