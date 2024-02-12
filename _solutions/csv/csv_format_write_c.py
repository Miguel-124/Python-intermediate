
result = ''
header = set()

def make_line(data):
    return ','.join(f'"{x}"' for x in data) + '\n'


for row in DATA:
    header.update(row.keys())

header = sorted(header)
result += make_line(header)

for row in DATA:
    line = [row.get(key, '') for key in header]
    result += make_line(line)
