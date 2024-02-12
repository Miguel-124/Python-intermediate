
result = []
header, *lines = DATA.splitlines()
header = header.strip().split(',')

for line in lines:
    line = line.strip().split(',')
    line = zip(header, line)
    result.append(dict(line))
