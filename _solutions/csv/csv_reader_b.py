
result = []

with open(FILE, mode='r') as file:
    reader = csv.reader(file, lineterminator='\n')

    for *features, label in reader:
        label = SPECIES[int(label)]
        row = tuple(features) + (label,)
        result.append(row)
