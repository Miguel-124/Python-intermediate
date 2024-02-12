
result = []
header, *lines = DATA.splitlines()
header = header.strip().split(',')
nrows, ncols, *class_labels = header
LABEL_ENCODER = dict(enumerate(class_labels))

for line in lines:
    *values, species = line.strip().split(',')
    species = LABEL_ENCODER[int(species)]
    row = tuple(values) + (species,)
    result.append(row)
