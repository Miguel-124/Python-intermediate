
result = [','.join(row.values()) for row in DATA]
result = '\n'.join(result)

# Alternative Solution
result = ''

for row in DATA:
    row = ','.join(row.values())
    result += str(row) + '\n'
