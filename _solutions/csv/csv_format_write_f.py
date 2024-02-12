
header = ','.join(vars(DATA[0]).keys())
rows = [','.join(map(str, vars(row).values())) for row in DATA]

data = []
data.append(header)
data.extend(rows)

result = '\n'.join(data) + '\n'


# Alternative solution
result = ''
data = [vars(x) for x in DATA]
header = data[0].keys()
result += ','.join(header) + '\n'

for row in data:
    row = map(str, row.values())
    result += ','.join(row) + '\n'
