
result = []

for line in DATA.splitlines():
    *values, species = line.strip().split(',')
    species = LABEL_ENCODER.get(species, species)
    row = tuple(values) + (species,)
    result.append(row)
