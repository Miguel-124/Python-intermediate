
result = []

with open(FILE, mode='r') as file:
    species = file.readline().strip().split(',')[2:]
    species = dict(enumerate(species))
    reader = csv.reader(file, lineterminator='\n')

    for *features, label in reader:
        label = species[int(label)]
        row = features + [label]
        result.append(tuple(row))
