
result = ''
header = DATA[0].keys()
result += ','.join(header) + '\n'

for row in DATA:
    row = map(str, row.values())
    result += ','.join(row) + '\n'

# Alternative solution
header = ','.join(DATA[0].keys())
rows = [','.join(map(str, row.values())) for row in DATA]

data = []
data.append(header)
data.extend(rows)

result = '\n'.join(data) + '\n'
