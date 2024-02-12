
data = []
with open(FILE) as file:
    for line in file:
        line = line.strip().split(',')
        data.append({
            'sepal_length': float(line[0]),
            'sepal_width': float(line[1]),
            'petal_length': float(line[2]),
            'petal_width': float(line[3]),
            'species': SPECIES[int(line[4])],
        })

with sqlite3.connect(DATABASE) as db:
    db.row_factory = sqlite3.Row
    db.execute(SQL_CREATE_TABLE)
    db.executemany(SQL_INSERT, data)
    result = [dict(x) for x in db.execute(SQL_SELECT)]
