
result = []

for line in DATA.splitlines():
    line = line.strip().split(',')
    line = dict(zip(HEADER, line))
    result.append(line)
