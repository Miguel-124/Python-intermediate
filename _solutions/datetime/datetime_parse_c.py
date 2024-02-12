
def parse(string):
    try:
        return datetime.strptime(string, '%B %dst, %Y')
    except ValueError:
        return datetime.strptime(string, '%B %dnd, %Y')

result = map(parse, DATA)


# Alternative
result = []

for line in DATA:
    try:
        dt = datetime.strptime(line, '%B %dst, %Y')
    except ValueError:
        dt = datetime.strptime(line, '%B %dnd, %Y')
    result.append(dt)
