
with open(FILE, mode='r') as file:
    result = [tuple(row.values()) for row in json.load(file)]
