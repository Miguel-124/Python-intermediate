
header, *rows = DATA
data = [dict(zip(header, row)) for row in rows]

with open(FILE, mode='w') as file:
    json.dump(data, file)
