
result = ''
firstname, lastname = DATA[0].keys()
result += f'"{firstname}","{lastname}"\n'

for row in DATA:
    firstname, lastname = row.values()
    result += f'"{firstname}","{lastname}"\n'


# Alternative Solution
def quote(sequence):
    return '"' + '","'.join(sequence) + '"'


header = quote(DATA[0].keys())
rows = [quote(row.values()) for row in DATA]

result = []
result.append(header)
result.extend(rows)
result = '\n'.join(result)
