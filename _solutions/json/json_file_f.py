
with open(FILE, mode='r') as file:
    data = json.load(file)

header = set()
for row in data:
    header.update(row.keys())
header = tuple(sorted(header))

rows = []
for row in data:
    values = {key: row.get(key, None) for key in header}
    rows.append(tuple(values.values()))


result = []
result.append(header)
result.extend(rows)
