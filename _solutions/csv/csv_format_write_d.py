
result = ''
for line in DATA:
    result += ','.join(str(x) for x in line) + '\n'
