
with open(FILE, mode='r') as file:
    data = json.load(file)

header = tuple(data[0].keys())
rows = [tuple(row.values()) for row in data]

result = []
result.append(header)
result.extend(rows)
