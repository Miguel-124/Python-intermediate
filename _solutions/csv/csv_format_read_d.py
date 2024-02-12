
result = []
header, *lines = DATA.splitlines()
header = header.strip().split(',')
result.append(tuple(header))

for line in lines:
    *values, species = line.strip().split(',')
    values = map(float, values)
    row = tuple(values) + (species,)
    result.append(row)
